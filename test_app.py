# test_app.py
import unittest
from app import app
import aws_controller

class TestStringMethods(unittest.TestCase):

<<<<<<< HEAD
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOxO')
=======
    assert response.status_code == 200
    
>>>>>>> 80f2c21dca0b5ff46fb73b3bd82a614cacc291d5


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