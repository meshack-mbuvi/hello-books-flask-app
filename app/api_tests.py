import unittest
import json

from run import create_app

# set global variables
BASE_URL = 'http://localhost:5000/api/v1/'
class BookAPITests(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app = self.app.test_client()

    def tearDown(self):
        self.app.testing = False
        self.app = None

    def test_get_all_books(self):
        # test for homepage
        resp = self.app.get(BASE_URL)
        self.assertEqual(resp.status_code, 200,
                         msg='Should retrieve data from the api.')

        data = json.loads(resp.get_data().decode('utf-8'))
        no_of_items = len(data)
        self.assertTrue(no_of_items != 0, msg = 'Should retrieve items')


if __name__ == '__main__':
    unittest.main()
