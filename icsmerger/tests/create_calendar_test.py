import unittest
import unittest.mock


from icsmerger import merge


class TestCreateCalendar(unittest.TestCase):

    @unittest.mock.patch("ics.Calendar")
    def test_craete(self, calendar_mock: unittest.mock.MagicMock):
        events = []
        merge.create_calendar(events)
        calendar_mock.assert_called_once_with(
            events=events)


if __name__ == "__main__":
    unittest.main()
