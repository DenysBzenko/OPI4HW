
import unittest
from unittest.mock import patch
from feature_one import app, delete_user_data_service

class FeatureOneTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    @patch.object(delete_user_data_service, 'delete_user_data_service')
    def test_forget_user_endpoint_success(self, mock_delete):
        # Test the successful deletion of user data
        mock_delete.return_value = True

        response = self.app.post('/api/user/forget?userId=123')
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['userId'], '123')
        mock_delete.assert_called_once_with('123')

    @patch.object(delete_user_data_service, 'delete_user_data_service')
    def test_forget_user_endpoint_failure(self, mock_delete):
        # Test the scenario where the deletion process fails
        mock_delete.return_value = False

        response = self.app.post('/api/user/forget?userId=123')
        data = response.get_json()

        self.assertEqual(response.status_code, 500)
        self.assertEqual(data['error'], 'An error occurred while processing the request')
        mock_delete.assert_called_once_with('123')

    def test_forget_user_endpoint_missing_userId(self):
        # Test the response when 'userId' is not provided
        response = self.app.post('/api/user/forget')
        data = response.get_json()

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['error'], 'userId is required')

if __name__ == '__main__':
    unittest.main()
