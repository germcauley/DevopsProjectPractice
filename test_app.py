# test_app.py
from app import app
import aws_controller

def test_apphomepage():
    response = app.test_client().get('/')

    assert response.status_code == 200
    

def test_appcommentpage1():
    response = app.test_client().get('/post')

    assert response.status_code == 200

def test_appcommentpage2():
    response = app.test_client().post('/post')

    assert response.status_code == 500

def test_appsuccesspage1():
    response = app.test_client().get('/success')

    assert response.status_code == 200
