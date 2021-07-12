import unittest
from main import app

class AppTest(unittest.TestCase):
    """Unit Testing"""
    def setUp(self):
        self.app = app.test_client()

    def test_base(self):
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)

