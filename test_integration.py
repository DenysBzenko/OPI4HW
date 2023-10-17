# test_integration.py
import unittest
from app import app

class TestIntegration(unittest.TestCase):
    def setUp(self):
        # Set up the test client.
        self.app = app.test_client()
        self.app.testing = True

    def test_get_total_online_time_integration(self):
        response = self.app.get('/api/stats/user/total?userId=1')
        self.assertEqual(response.status_code, 200)
        self.assertIn('totalTime', str(response.data))

    def test_user_average_time_integration(self):
        response = self.app.get('/api/stats/user/average?userId=1')
        self.assertEqual(response.status_code, 200)
        self.assertIn('weeklyAverage', str(response.data))
        self.assertIn('dailyAverage', str(response.data))

    def test_forget_user_integration(self):
        response = self.app.post('/api/user/forget?userId=1')
        self.assertEqual(response.status_code, 200)
        self.assertIn('userId', str(response.data))

if __name__ == '__main__':
    unittest.main()
