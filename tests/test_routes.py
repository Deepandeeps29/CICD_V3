import requests

BASE_URL = "http://127.0.0.1:5000"

def test_home():
    response = requests.get(f"{BASE_URL}/")
    assert response.status_code == 200
    assert "Welcome to the Home Page" in response.text

def test_login():
    response = requests.get(f"{BASE_URL}/login")
    assert response.status_code == 200
    assert "Login Page" in response.text
