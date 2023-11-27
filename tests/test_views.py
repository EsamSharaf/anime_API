import json
from .factories import AnimeFactory
from .db_test import db


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


def test_anime_by_name_route(client):
    AnimeFactory(
        anime_id=1535,
        name='Death Note',
        genre='Mystery, Police, Psychological, Supernatural, Thriller',
        type='TV',
        episodes='37',
        rating=8.71,
        members=1013917,
    )
    db.session.commit()

    response = client.get('/api/v1/anime/Death Note')
    assert response.status_code == 200
    assert json.loads(response.get_data()) == {

            "anime_id": 1535, "episodes": 37,
            "genre": "Mystery, Police, Psychological, Supernatural, Thriller",
            "members": 1013917, "name": "Death Note",
            "rating": 8.71, "type": "TV"
    }
