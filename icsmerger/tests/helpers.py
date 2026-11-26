"""
Helpers to build ICS feeds and fake HTTP responses for the tests.
"""
import requests


def make_ics(*events: tuple) -> str:
    """
    Builds an ICS from (uid, summary) tuples.
    """
    lines = ["BEGIN:VCALENDAR", "VERSION:2.0", "PRODID:-//test//EN"]
    for uid, summary in events:
        lines += [
            "BEGIN:VEVENT",
            f"UID:{uid}",
            "DTSTAMP:20260101T000000Z",
            "DTSTART:20260102T100000Z",
            "DTEND:20260102T110000Z",
            f"SUMMARY:{summary}",
            "END:VEVENT",
        ]
    lines.append("END:VCALENDAR")
    return "\r\n".join(lines) + "\r\n"


def make_response(body=b"", status=200, content_type="text/calendar") -> requests.Response:
    """
    Builds a real requests.Response, so raise_for_status() and text work as in production.
    """
    response = requests.Response()
    response.status_code = status
    response.reason = "Test"
    response.url = "https://feed.test/"
    response._content = body.encode("utf-8") if isinstance(body, str) else body
    if content_type is not None:
        response.headers["Content-Type"] = content_type
    response.encoding = requests.utils.get_encoding_from_headers(response.headers)
    return response
