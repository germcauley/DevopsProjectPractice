# test_app.py
import unittest
from application import app
import aws_controller

class TestStringMethods(unittest.TestCase):


    # Some basic unittests

    def test_apphomepage(self):
        response = app.test_client().get('/')

        self.assertEqual(response.status_code,200)
        

    def test_appcommentpage1(self):
        response = app.test_client().get('/post')

        self.assertEqual(response.status_code,200)

    # def test_appcommentpage2(self):
    #     response = app.test_client().post('/post')

    #     self.assertEqual(response.status_code,500)

    def test_appsuccesspage1(self):
        response = app.test_client().get('/success')

        self.assertEqual(response.status_code,200)

if __name__ == '__main__':
    unittest.main()
