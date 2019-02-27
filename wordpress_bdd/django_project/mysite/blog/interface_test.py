import requests
import unittest

class test_blog_data(object):
    def setUp(self):
        self.base_url = 'http://127.0.0.1:8000/'

    def test_blog_data(self):
        r = requests.get(self.base_url + 'blog_data')
        code = r.status_code
        self.assertEqual(code, 200)

    def tearDown(self):
            pass

if __name__ == '__main__':
    unittest.main()