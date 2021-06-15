import unittest
import unittest.mock

import click.testing

from icsmerger import merge


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
        get_ics_mock.assert_called_once_with(url, True)
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
        get_ics_mock.assert_called_once_with(url, True)
        get_events_mock.assert_called_once_with(ics_content)
        create_calendar_mock.assert_called_once_with(events)
        print_mock.assert_not_called()
        save_calendar_mock.assert_called_once_with(calendar_str, out)

    @unittest.mock.patch("builtins.print")
    @unittest.mock.patch("ics.Calendar")
    @unittest.mock.patch("icsmerger.merge.create_calendar")
    @unittest.mock.patch("icsmerger.merge.get_events")
    @unittest.mock.patch("icsmerger.merge.get_ics")
    def test_with_ingore_http_error_option(self, get_ics_mock: unittest.mock.MagicMock, get_events_mock: unittest.mock.MagicMock, create_calendar_mock: unittest.mock.MagicMock, calendar_mock: unittest.mock.MagicMock, print_mock: unittest.mock.MagicMock):
        url = "http://foo.bar"
        arguments = [
            "--ignore-http-errors",
            url,
        ]

        runner = click.testing.CliRunner()
        runner.invoke(merge.main, arguments)
        get_ics_mock.assert_called_once_with(url, False)


if __name__ == "__main__":
    unittest.main()
