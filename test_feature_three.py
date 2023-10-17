import unittest
from unittest.mock import patch
from feature_three import app

class FeatureThreeTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    @patch('feature_three.get_total_online_time')
    def test_user_total_time(self, mock_total_time):
        mock_total_time.return_value = 2344242223423

        response = self.app.get('/api/stats/user/total?userId=123')
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['totalTime'], 2344242223423)
        mock_total_time.assert_called_once_with('123')

    def test_user_total_time_no_userId(self):
        response = self.app.get('/api/stats/user/total')
        data = response.get_json()

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['error'], 'userId is required')

if __name__ == '__main__':
    unittest.main()
