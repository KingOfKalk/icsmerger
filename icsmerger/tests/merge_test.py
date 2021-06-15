import unittest
import unittest.mock

import click.testing

from icsmerger import merge


class TestCreateCalendar(unittest.TestCase):

    @unittest.mock.patch("ics.Calendar")
    def test_craete(self, calendar_mock: unittest.mock.MagicMock):
        events = []
        merge.create_calendar(events)
        calendar_mock.assert_called_once_with(
            events=events)


class TestGetEvents(unittest.TestCase):

    @unittest.mock.patch("ics.Calendar")
    def test_calendar_is_used(self, calendar_mock: unittest.mock.MagicMock):
        content = "no real content"
        merge.get_events(content)
        calendar_mock.assert_called_once_with(content)

    @unittest.mock.patch("ics.Calendar")
    def test_calendar_events_are_used(self, calendar_mock: unittest.mock.MagicMock):
        event = "a event"
        events = [event]
        content = "no real content"

        type(calendar_mock.return_value).events = events

        actual_events = merge.get_events(content)
        calendar_mock.assert_called_once_with(content)
        self.assertListEqual(actual_events, events)


class TestGetIcs(unittest.TestCase):

    @unittest.mock.patch("requests.get")
    def test_calls_requests_get(self, get_mock: unittest.mock.MagicMock):
        url = "https://python.org"
        merge.get_ics(url)
        get_mock.assert_called_once_with(url)

    @unittest.mock.patch("requests.Response")
    @unittest.mock.patch("requests.get")
    def test_returns_text_from_repsonse_if_200(self, get_mock: unittest.mock.MagicMock, response_mock: unittest.mock.MagicMock):
        expected_text = "lorem ipmsum"

        response_mock.status_code = 200
        response_mock.text = expected_text

        get_mock.return_value = response_mock

        actual_text = merge.get_ics("https://python.org")
        self.assertEqual(actual_text, expected_text)

    @unittest.mock.patch("requests.Response")
    @unittest.mock.patch("requests.get")
    def test_returns_empty_string_status_code_is_not_200(self, get_mock: unittest.mock.MagicMock, response_mock: unittest.mock.MagicMock):
        expected_text = ""

        response_mock.status_code = 100
        response_mock.text = expected_text

        get_mock.return_value = response_mock

        actual_text = merge.get_ics("https://python.org")
        self.assertEqual(actual_text, expected_text)


class TestMain(unittest.TestCase):
    """
    See https://click.palletsprojects.com/en/8.0.x/testing/
    """

    @unittest.mock.patch("builtins.print")
    @unittest.mock.patch("ics.Calendar")
    @unittest.mock.patch("icsmerger.merge.create_calendar")
    @unittest.mock.patch("icsmerger.merge.get_events")
    @unittest.mock.patch("icsmerger.merge.get_ics")
    def test_without_out(self, get_ics_mock: unittest.mock.MagicMock, get_events_mock: unittest.mock.MagicMock, create_calendar_mock: unittest.mock.MagicMock, calendar_mock: unittest.mock.MagicMock, print_mock: unittest.mock.MagicMock):
        url = "http://foo.bar"
        arguments = [
            url,
        ]
        ics_content = "foo"
        get_ics_mock.return_value = ics_content
        event = "a event"
        events = [event]
        get_events_mock.return_value = events

        calendar_str = "bar"
        create_calendar_mock.return_value = calendar_str

        runner = click.testing.CliRunner()
        actual = runner.invoke(merge.main, arguments)
        self.assertEqual(actual.exit_code, 0)
        self.assertEqual(actual.output, "")
        get_ics_mock.assert_called_once_with(url)
        get_events_mock.assert_called_once_with(ics_content)
        create_calendar_mock.assert_called_once_with(events)
        print_mock.assert_called_once_with(calendar_str)

    @unittest.mock.patch("builtins.print")
    @unittest.mock.patch("icsmerger.merge.save_calendar")
    @unittest.mock.patch("icsmerger.merge.create_calendar")
    @unittest.mock.patch("icsmerger.merge.get_events")
    @unittest.mock.patch("icsmerger.merge.get_ics")
    def test_with_out(self, get_ics_mock: unittest.mock.MagicMock, get_events_mock: unittest.mock.MagicMock, create_calendar_mock: unittest.mock.MagicMock, save_calendar_mock: unittest.mock.MagicMock, print_mock: unittest.mock.MagicMock):
        url = "http://foo.bar"
        out = 'test.ics'
        arguments = [
            url,
            '--out',
            out
        ]
        ics_content = "foo"
        get_ics_mock.return_value = ics_content
        event = "a event"
        events = [event]
        get_events_mock.return_value = events

        calendar_str = "bar"
        create_calendar_mock.return_value = calendar_str

        runner = click.testing.CliRunner()
        actual = runner.invoke(merge.main, arguments)
        self.assertEqual(actual.exit_code, 0)
        self.assertEqual(actual.output, "")
        get_ics_mock.assert_called_once_with(url)
        get_events_mock.assert_called_once_with(ics_content)
        create_calendar_mock.assert_called_once_with(events)
        print_mock.assert_not_called()
        save_calendar_mock.assert_called_once_with(calendar_str, out)


class TestSaveCalendar(unittest.TestCase):

    @unittest.mock.patch("icsmerger.merge.open", new_callable=unittest.mock.mock_open(), create=True)
    @unittest.mock.patch("ics.Calendar")
    def test_save(self, calendar_mock: unittest.mock.MagicMock, open_mock: unittest.mock.MagicMock):
        expected_out = "calendar.ics"
        expected_write = "ics data"
        calendar_mock.__str__ = unittest.mock.MagicMock(
            return_value=expected_write)
        merge.save_calendar(calendar_mock, expected_out)
        open_mock.assert_called_with(expected_out, "w")
        handle = open_mock()
        handle.__enter__().write.assert_called_once_with(expected_write)


if __name__ == "__main__":
    unittest.main()
