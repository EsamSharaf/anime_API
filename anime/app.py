from flask import Flask

from anime.extensions import db
from anime.settings import DevConfig
from anime.views import animes_bp


def create_app(config_object=DevConfig):

    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    register_blueprints(app)

    return app

def register_extensions(app):
    """Register Flask extensions."""

    db.init_app(app)
    with app.app_context():
        db.reflect()

def register_blueprints(app):
    """Register Flask blueprints."""

    app.register_blueprint(animes_bp)
