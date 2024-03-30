import pytest
from flask_jwt_extended import create_access_token

from anime.app import create_app, db
from anime.settings import TestConfig

from .factories import AnimeFactory, UserFactory


@pytest.fixture()
def app():

    # create the app
    app = create_app(TestConfig)

    with app.app_context():

        db.create_all()

        yield app

        db.drop_all()
        db.session.close()


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()


@pytest.fixture()
def create_default_anime(app):
    return AnimeFactory()


@pytest.fixture()
def create_default_user(app):
    return UserFactory()


@pytest.fixture()
def test_header(app):
    token = create_access_token(identity="default_user")

    header = {
        'Authorization': 'Bearer {}'.format(token)
    }

    return header
