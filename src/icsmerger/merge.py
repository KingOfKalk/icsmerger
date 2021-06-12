"""
Grabs ICS from the internat and merges them together.
"""
import click
import ics
import requests
import typing


def get_ics(url: str) -> str:
    """
    Returns the ICS content.
    """
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return ""


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


def save_calendar(calendar: ics.Calendar, out: str) -> None:
    """
    Saves the calendar to a file.
    """
    with open(out, "w") as f:
        f.write(str(calendar))


@click.command(context_settings=dict(help_option_names=["-h", "--help"]))
@click.argument('urls', nargs=-1, required=True)
@click.option("-o", "--out", help="Path to save the result. If not set, STDOUT will be used.")
def main(urls, out):
    events = []
    for url in urls:
        content = get_ics(url)
        events += get_events(content)
    calendar = create_calendar(events)
    if out is None:
        print(calendar)
    else:
        save_calendar(calendar, out)
