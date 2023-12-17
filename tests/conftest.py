import pytest
from conduit.app import create_app
from conduit.database import db as _db
from conduit.settings import TestConfig
from .factories import AnimeFactory


@pytest.fixture()
def app():

    # create the app
    _app = create_app(TestConfig)

    with _app.app_context():

        _db.create_all()

        yield app

        _db.drop_all()


@pytest.fixture()
def db(app):
    """A database for the tests."""
    _db.app = app

    with app.app_context():
        _db.create_all()

    yield _db

    # Explicitly close DB connection
    _db.session.close()
    _db.drop_all()


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()


@pytest.fixture()
def create_default_anime(db):
    return AnimeFactory()
