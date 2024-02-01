from anime.app import db
from anime.schemas import AnimeSchema
from .factories import AnimeFactory


def test_animes_route(client, create_default_anime):
    AnimeFactory(
        anime_id=111222,
        name='anime_1',
        genre='Horror',
        type='TV',
        episodes='27',
        rating=8.5,
        members=1256,
    )
    db.session.commit()

    response = client.get('/api/v1/animes/')

    anime_schema = AnimeSchema()

    assert response.status_code == 200
    assert anime_schema.loads(response.get_data(), many=True) == [
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


def test_get_anime_by_name_route(client, create_default_anime):
    AnimeFactory(
        anime_id=1535,
        name='Death Note',
        genre='Mystery, Police, Psychological, Supernatural, Thriller',
        type='TV',
        episodes=37,
        rating=8.71,
        members=1013917,
    )
    db.session.commit()

    anime_schema = AnimeSchema()

    response = client.get('/api/v1/anime/Death Note')

    assert response.status_code == 200
    assert anime_schema.loads(response.get_data()) == {
        "anime_id": 1535, "episodes": 37,
        "genre": "Mystery, Police, Psychological, Supernatural, Thriller",
        "members": 1013917, "name": "Death Note",
        "rating": 8.71, "type": "TV"
    }


def test_get_anime_by_name_route_anime_not_found(client, create_default_anime):
    response = client.get('/api/v1/anime/Kokami')

    assert response.status_code == 404

def test_anime_patch(client, create_default_anime):

    anime_schema = AnimeSchema()

    response = client.patch('/api/v1/animes/11', json={
        "episodes": 30,
        "rating": 7.5,
    })

    assert response.status_code == 200
    assert anime_schema.loads(response.data) == {
        "anime_id": 11,
        "name": "anime_default",
        "genre": "Action",
        "type": "TV",
        "episodes": 30,
        "rating": 7.5,
        "members": 123456
    }
 
def test_anime_delete(client, create_default_anime):
    response = client.delete('/api/v1/animes/11')

    assert response.status_code == 204


def test_anime_delete_not_found(client, create_default_anime):
    response = client.delete('/api/v1/animes/10')

    assert response.status_code == 404