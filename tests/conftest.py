import pytest
from flask import Flask

from views import config_routes

from .db_test import db
from .factories import AnimeFactory


@pytest.fixture()
def app():

    # create the app
    app = Flask(__name__)

    app.config.update({
        "TESTING": True,
    })

    # configure the SQLite database for testing
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///animeDB_test.db"

    # initialize the app with the extension
    db.init_app(app)

    with app.app_context():

        db.create_all()
        animes_bp = config_routes(db)
        app.register_blueprint(animes_bp)

        yield app

        db.drop_all()


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()


@pytest.fixture()
def create_default_anime(app):
    return AnimeFactory()
