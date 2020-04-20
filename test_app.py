# test_app.py
import unittest
from app import app
import aws_controller

class TestStringMethods(unittest.TestCase):


    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOxO')



    # def test_apphomepage(self):
    #     response = app.test_client().get('/')

    #     assert response.status_code == 404
        

    # def test_appcommentpage1():
    #     response = app.test_client().get('/post')

    #     assert response.status_code == 200

    # def test_appcommentpage2():
    #     response = app.test_client().post('/post')

    #     assert response.status_code == 500

    # def test_appsuccesspage1():
    #     response = app.test_client().get('/success')

    #     assert response.status_code == 200
if __name__ == '__main__':
    unittest.main()
