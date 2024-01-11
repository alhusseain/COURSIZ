import unittest
from unittest.mock import patch
from meetings import get_country_code, get_timezone_offset, generate_iso_format, create_teams_meeting

class TestMeetings(unittest.TestCase):

    def test_get_country_code(self):
        # Test case for existing country
        self.assertEqual(get_country_code("Egypt"), "EG")
        
        # Test case for non-existing country
        self.assertIsNone(get_country_code("NonExistingCountry"))

    def test_get_timezone_offset(self):
        # Test case for existing country
        self.assertIsNotNone(get_timezone_offset("EG"))
        
        # Test case for non-existing country
        self.assertIsNone(get_timezone_offset("NonExistingCountry"))

    def test_generate_iso_format(self):
        # Test case for generating ISO format
        iso_format = generate_iso_format(2022, 3, 25, 12, 30)
        self.assertEqual(iso_format, "2022-03-25T12:30:00.000+02:00")

    @patch('meetings.requests.request')
    def test_create_teams_meeting(self, mock_request):
        # Mocking the request to Microsoft Graph API
        mock_request.return_value.status_code = 201
        mock_request.return_value.json.return_value = {'joinWebUrl': 'https://example.com/meeting'}

        # Test case for successful meeting creation
        meeting_url = create_teams_meeting("token", "user_id", 2022, 3, 25, 2022, 3, 25, 12, 30, 1, 1, "Egypt", "User Meeting")
        self.assertEqual(meeting_url, 'https://example.com/meeting')

        # Test case for unsuccessful meeting creation
        mock_request.return_value.status_code = 400
        meeting_url = create_teams_meeting("token", "user_id", 2022, 3, 25, 2022, 3, 25, 12, 30, 1, 1, "Egypt", "User Meeting")
        self.assertIsNone(meeting_url)

if __name__ == '__main__':
    unittest.main()