import factory

from models import Anime

from .conftest import db


class AnimeFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Anime
        sqlalchemy_session = db.session

    anime_id = 11
    name = 'anime_default'
    genre = 'Action'
    type = 'TV'
    episodes = '27'
    rating = 8.0
    members = 123456
