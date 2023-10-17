
import unittest
import requests

class TestEndToEnd(unittest.TestCase):

    BASE_URL = 'http://localhost:5000'

    def test_total_online_time_e2e(self):
        user_id = '1'
        response = requests.get(f'{self.BASE_URL}/api/stats/user/total?userId={user_id}')
        self.assertEqual(response.status_code, 200)
        self.assertIn('totalTime', response.json())

    def test_user_average_time_e2e(self):
        user_id = '1'
        response = requests.get(f'{self.BASE_URL}/api/stats/user/average?userId={user_id}')
        self.assertEqual(response.status_code, 200)
        self.assertIn('weeklyAverage', response.json())
        self.assertIn('dailyAverage', response.json())

    def test_forget_user_e2e(self):
        user_id = '1'
        response = requests.post(f'{self.BASE_URL}/api/user/forget?userId={user_id}')
        self.assertEqual(response.status_code, 200)
        self.assertIn('userId', response.json())

if __name__ == '__main__':
    unittest.main()
