import factory
from werkzeug.security import generate_password_hash

from anime.models import Anime, User

from .conftest import db


class AnimeFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Anime
        sqlalchemy_session = db.session
        sqlalchemy_session_persistence = 'commit'

    anime_id = 11
    name = 'anime_default'
    genre = 'Action'
    type = 'TV'
    episodes = 27
    rating = 8.0
    members = 123456


class UserFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = User
        sqlalchemy_session = db.session
        sqlalchemy_session_persistence = 'commit'

    id = 1
    username = 'default_user'
    password = generate_password_hash('default_password')
