"""
Grabs ICS from the internat and merges them together.
"""
import typing


import click
import ics
import requests


# (connect, read) timeout in seconds
TIMEOUT = (5, 30)


def _fail(url: str, error: Exception, exit_on_http_errors: bool) -> None:
    """
    Raises a ClickException (exit code 1) or, if errors are ignored,
    prints a warning to stderr so the feed can be skipped.
    """
    if exit_on_http_errors:
        raise click.ClickException(f"{url}: {error}") from error
    click.echo(f"Warning: skipping {url}: {error}", err=True)


def _decode(response: requests.Response) -> str:
    """
    Decodes the response body. RFC 5545 makes UTF-8 the default, but requests
    assumes ISO-8859-1 for text/* without a charset.
    """
    if "charset" not in response.headers.get("Content-Type", "").lower():
        try:
            return response.content.decode("utf-8-sig")
        except UnicodeDecodeError:
            pass
    return response.text


def get_ics(url: str, exit_on_http_errors: bool = True) -> typing.Optional[str]:
    """
    Returns the ICS content.
    Returns None if the request failed and errors are ignored.
    """
    try:
        response = requests.get(url, timeout=TIMEOUT)
        response.raise_for_status()
        if response.status_code != 200:
            raise requests.exceptions.HTTPError(
                f"unexpected status code {response.status_code}", response=response)
    except requests.exceptions.RequestException as e:
        _fail(url, e, exit_on_http_errors)
        return None
    return _decode(response)


def get_events(content: str) -> typing.List[ics.Event]:
    """
    Extracts all events from an ICS.
    """
    events = []
    calendar = ics.Calendar(content)
    for event in calendar.events:
        events.append(event)
    return events


def create_calendar(events: typing.List[ics.Event]) -> ics.Calendar:
    """
    Creates a new calender and adds all the given events.
    """
    calendar = ics.Calendar(events=events)
    return calendar


def save_calendar(text: str, out: str) -> None:
    """
    Saves the serialized calendar to a file.
    """
    with open(out, "w", encoding="utf-8", newline="") as f:
        f.write(text)


@click.command(context_settings=dict(help_option_names=["-h", "--help"]))
@click.argument('urls', nargs=-1, required=True)
@click.option("-o", "--out", help="Path to save the result. If not set, STDOUT will be used.")
@click.option('--exit-on-http-errors/--ignore-http-errors',
              help="Exit and returns error code when a feed cannot be fetched or parsed. "
              "With --ignore-http-errors such feeds are skipped with a warning.",
              default=True)
def main(urls, out, exit_on_http_errors):
    events = []
    for url in urls:
        content = get_ics(url, exit_on_http_errors)
        if content is None:
            continue
        try:
            events += get_events(content)
        except Exception as e:
            _fail(url, e, exit_on_http_errors)
    text = create_calendar(events).serialize()
    if out is None:
        click.echo(text, nl=False)
    else:
        save_calendar(text, out)
