
import unittest
from unittest.mock import patch
from feature_two import app, get_weekly_online_time_service, get_daily_online_time_service

class FeatureTwoTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    @patch.object(get_weekly_online_time_service, 'get_weekly_online_time_service')
    @patch.object(get_daily_online_time_service, 'get_daily_online_time_service')
    def test_user_average_time_endpoint_success(self, mock_daily, mock_weekly):
        # Test the successful retrieval of user average time
        mock_weekly.return_value = 119000
        mock_daily.return_value = 3200

        response = self.app.get('/api/stats/user/average?userId=123')
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['weeklyAverage'], 17000)
        self.assertEqual(data['dailyAverage'], 3200)
        mock_weekly.assert_called_once_with('123')
        mock_daily.assert_called_once_with('123')

    def test_user_average_time_endpoint_missing_userId(self):
        # Test the response when 'userId' is not provided
        response = self.app.get('/api/stats/user/average')
        data = response.get_json()

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['error'], 'userId is required')

if __name__ == '__main__':
    unittest.main()
