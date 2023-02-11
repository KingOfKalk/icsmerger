import unittest
import unittest.mock

from icsmerger import merge


class TestSaveCalendar(unittest.TestCase):

    @unittest.mock.patch("icsmerger.merge.open", new_callable=unittest.mock.mock_open(), create=True)
    @unittest.mock.patch("ics.Calendar")
    def test_save(self, calendar_mock: unittest.mock.MagicMock, open_mock: unittest.mock.MagicMock):
        expected_out = "calendar.ics"
        expected_write = "ics data"
        calendar_mock.serialize = unittest.mock.MagicMock(
            return_value=expected_write)
        merge.save_calendar(calendar_mock, expected_out)
        open_mock.assert_called_with(expected_out, "w")
        handle = open_mock()
        handle.__enter__().write.assert_called_once_with(expected_write)


if __name__ == "__main__":
    unittest.main()
