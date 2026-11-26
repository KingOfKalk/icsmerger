import unittest.mock

import click
import pytest
import requests

from icsmerger import merge
from icsmerger.tests.helpers import make_ics, make_response

URL = "https://feed.test/one.ics"


def patch_get(**kwargs):
    return unittest.mock.patch("requests.get", **kwargs)


def test_calls_requests_get_with_timeout():
    with patch_get(return_value=make_response(make_ics())) as get_mock:
        merge.get_ics(URL)
    get_mock.assert_called_once_with(URL, timeout=(5, 30))


def test_returns_text():
    content = make_ics(("1", "Hello"))
    with patch_get(return_value=make_response(content)):
        assert merge.get_ics(URL) == content


def test_utf8_without_charset():
    content = make_ics(("1", "Müller Straße Café"))
    with patch_get(return_value=make_response(content, content_type="text/calendar")):
        assert merge.get_ics(URL) == content


def test_utf8_bom_is_removed():
    content = make_ics(("1", "Hello"))
    with patch_get(return_value=make_response("﻿" + content)):
        assert merge.get_ics(URL) == content


def test_charset_is_respected():
    content = make_ics(("1", "Müller"))
    response = make_response(content.encode("iso-8859-1"), content_type="text/calendar; charset=iso-8859-1")
    with patch_get(return_value=response):
        assert merge.get_ics(URL) == content


def test_invalid_utf8_without_charset_falls_back_to_response_text():
    content = make_ics(("1", "Müller"))
    with patch_get(return_value=make_response(content.encode("iso-8859-1"))):
        assert merge.get_ics(URL) == content


@pytest.mark.parametrize("status", [100, 204, 301, 404, 500])
def test_non_200_raises_click_exception(status):
    with patch_get(return_value=make_response(status=status)):
        with pytest.raises(click.ClickException) as error:
            merge.get_ics(URL)
    assert URL in error.value.format_message()


@pytest.mark.parametrize("error", [
    requests.exceptions.ConnectionError("refused"),
    requests.exceptions.Timeout("too slow"),
])
def test_request_error_raises_click_exception(error):
    with patch_get(side_effect=error):
        with pytest.raises(click.ClickException) as raised:
            merge.get_ics(URL)
    assert raised.value.format_message() == f"{URL}: {error}"


@pytest.mark.parametrize("status", [100, 204, 301, 404, 500])
def test_ignored_status_returns_none_and_warns(status, capsys):
    with patch_get(return_value=make_response(status=status)):
        assert merge.get_ics(URL, False) is None
    assert URL in capsys.readouterr().err


def test_ignored_request_error_returns_none_and_warns(capsys):
    with patch_get(side_effect=requests.exceptions.Timeout("too slow")):
        assert merge.get_ics(URL, False) is None
    captured = capsys.readouterr()
    assert URL in captured.err
    assert "too slow" in captured.err
    assert captured.out == ""
