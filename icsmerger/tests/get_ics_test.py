import unittest
import unittest.mock
import requests.exceptions

from icsmerger import merge


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

    @unittest.mock.patch("sys.exit")
    @unittest.mock.patch("requests.Response")
    @unittest.mock.patch("requests.get")
    def test_exits_with_error_code_when_http_error_occured(self, get_mock: unittest.mock.MagicMock, response_mock: unittest.mock.MagicMock, sys_exit_mock: unittest.mock.MagicMock):

        response_mock.status_code = 500

        get_mock.return_value = response_mock

        merge.get_ics("https://python.org", True)
        sys_exit_mock.assert_called_once_with(1)

    @unittest.mock.patch("sys.exit")
    @unittest.mock.patch("requests.get")
    def test_exits_when_requests_throws_an_eception_and_exit_on_error_is_set(self, get_mock: unittest.mock.MagicMock, sys_exit_mock: unittest.mock.MagicMock):
        get_mock.side_effect = requests.exceptions.RequestException('Kaputt')
        with self.assertRaises(SystemExit) as context:
            merge.get_ics("https://python.org", True)
            self.assertTrue('Kaputt' in context.exception)


if __name__ == "__main__":
    unittest.main()
