"""
Round-trip tests through the CLI with real ICS parsing and serialising.
Only requests.get is mocked.
"""
import unittest.mock
import warnings

import click.testing
import pytest
import requests

from icsmerger import merge
from icsmerger.tests.helpers import make_ics, make_response

GOOD = "https://feed.test/good.ics"
GOOD2 = "https://feed.test/good2.ics"
BAD = "https://feed.test/bad.ics"

FAILURES = {
    "404": lambda: make_response("Not found", status=404, content_type="text/plain"),
    "204": lambda: make_response(b"", status=204, content_type=None),
    "html": lambda: make_response("<html><body>Login</body></html>", content_type="text/html"),
    "connection-refused": lambda: requests.exceptions.ConnectionError("Connection refused"),
    "timeout": lambda: requests.exceptions.Timeout("Read timed out"),
}


def run(feeds: dict, *args):
    """
    Invokes the CLI; feeds maps URL to a Response or an exception to raise.
    """
    def fake_get(url, **kwargs):
        feed = feeds[url]
        if isinstance(feed, Exception):
            raise feed
        return feed

    with unittest.mock.patch("requests.get", side_effect=fake_get):
        return click.testing.CliRunner().invoke(merge.main, [*args, *feeds])


def summaries(output: str) -> list:
    return sorted(line[len("SUMMARY:"):] for line in output.splitlines() if line.startswith("SUMMARY:"))


def test_two_feeds_are_merged():
    result = run({
        GOOD: make_response(make_ics(("1", "One"))),
        GOOD2: make_response(make_ics(("2", "Two"), ("3", "Three"))),
    })
    assert result.exit_code == 0
    assert summaries(result.stdout) == ["One", "Three", "Two"]
    assert result.stderr == ""


def test_utf8_without_charset_on_stdout_and_in_file(tmp_path):
    feeds = {GOOD: make_response(make_ics(("1", "Müller Straße Café")), content_type="text/calendar")}
    result = run(feeds)
    assert result.exit_code == 0
    assert "SUMMARY:Müller Straße Café" in result.stdout

    out = tmp_path / "out.ics"
    result = run(feeds, "-o", str(out))
    assert result.exit_code == 0
    assert "SUMMARY:Müller Straße Café" in out.read_text(encoding="utf-8")


def test_stdout_and_file_are_identical_and_warning_free(tmp_path):
    def feeds():
        return {GOOD: make_response(make_ics(("1", "One"), ("2", "Two")))}

    out = tmp_path / "out.ics"
    with warnings.catch_warnings():
        warnings.simplefilter("error", FutureWarning)
        stdout_result = run(feeds())
        file_result = run(feeds(), "-o", str(out))
    assert stdout_result.exit_code == 0
    assert file_result.exit_code == 0
    assert stdout_result.stdout_bytes == out.read_bytes()
    assert stdout_result.stderr == ""
    assert file_result.stdout == ""


@pytest.mark.parametrize("failure", FAILURES)
def test_failure_exits_with_message_naming_the_url(failure):
    result = run({GOOD: make_response(make_ics(("1", "One"))), BAD: FAILURES[failure]()})
    assert result.exit_code == 1
    assert result.stdout == ""
    assert result.stderr.startswith(f"Error: {BAD}: ")


@pytest.mark.parametrize("failure", FAILURES)
def test_ignore_http_errors_skips_the_failed_feed(failure):
    result = run({GOOD: make_response(make_ics(("1", "One"))), BAD: FAILURES[failure]()}, "--ignore-http-errors")
    assert result.exit_code == 0
    assert summaries(result.stdout) == ["One"]
    assert BAD in result.stderr
    assert GOOD not in result.stderr


@pytest.mark.parametrize("failure", FAILURES)
def test_ignore_http_errors_with_all_feeds_failing_gives_empty_calendar(failure, tmp_path):
    feeds = {BAD: FAILURES[failure](), GOOD: FAILURES[failure]()}
    result = run(feeds, "--ignore-http-errors")
    assert result.exit_code == 0
    assert "BEGIN:VCALENDAR" in result.stdout
    assert "BEGIN:VEVENT" not in result.stdout
    assert BAD in result.stderr
    assert GOOD in result.stderr

    out = tmp_path / "out.ics"
    result = run(feeds, "--ignore-http-errors", "-o", str(out))
    assert result.exit_code == 0
    assert "BEGIN:VCALENDAR" in out.read_text(encoding="utf-8")
