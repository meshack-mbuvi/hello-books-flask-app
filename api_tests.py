import unittest
import json

from app import app

#set global variables
BASE_URL = 'http://localhost:5000/api/v1/books'

class BookAPITests(unittest.TestCase):
	def setUp(self):
		self.app = app
		self.app = app.test_client()
		self.app.testing = True

	def tearDown(self):
		self.app.testing = False

	
	def test_get_all_books(self):
		#test for homepage
		resp = self.app.get(BASE_URL)
		self.assertEqual(resp.status_code, 200, msg = 'Should retrieve all books.')
	


if __name__ == '__main__':
	unittest.main()