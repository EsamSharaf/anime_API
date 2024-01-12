import pytest
from anime.app import create_app
from anime.app import db
from anime.settings import TestConfig
from .factories import AnimeFactory


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
