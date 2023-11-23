import json


def test_animes_route(client):

    response = client.get('/api/v1/animes/')
    assert response.status_code == 200
    assert json.loads(response.get_data()) == [
        {
            "anime_id": 111222, "episodes": 27, "genre": "Horror",
            "members": 1256, "name": "anime_1", "rating": 8.5, "type": "TV"
        },
        {
            "anime_id": 11, "episodes": 27, "genre": "Action",
            "members": 123456, "name": "anime_default", "rating": 8.0,
            "type": "TV"
        },
    ]
