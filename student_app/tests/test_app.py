import pytest
from app import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Students' in response.data

def test_add_student(client):
    response = client.post('/add', data={'name': 'Alice', 'roll': '101'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Alice' in response.data
