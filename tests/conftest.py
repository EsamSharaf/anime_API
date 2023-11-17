import pytest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from models import Base

from .factories import AnimeFactory


@pytest.fixture()
def app():

    db = SQLAlchemy(model_class=Base)

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

        db.session.add(AnimeFactory())
        db.session.add(AnimeFactory(
            anime_id=111222,
            name='anime_1',
            genre='Horror',
            type='TV',
            episodes='27',
            rating=8.5,
            members=1256,
            )
        )

        db.session.commit()

        from views import config_routes

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
