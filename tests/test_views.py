from app import app


def test_animes_route():
    client = app.test_client()
    response = client.get('/api/v1/animes/')
    assert response.status_code == 200
