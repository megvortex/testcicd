from app import app

def test_index():
    client = app.test_client()
    response = client.get('/')
    assert response.data == b"Hello, DevOps!"

def test_about():
    client = app.test_client()
    response = client.get('/about')
    assert response.status_code == 200
