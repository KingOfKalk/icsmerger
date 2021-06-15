
import unittest
import unittest.mock

from icsmerger import merge


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


if __name__ == "__main__":
    unittest.main()
