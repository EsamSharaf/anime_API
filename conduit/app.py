from flask import Flask

from conduit.extensions import db
from conduit.settings import DevConfig
from conduit.views import animes_bp


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
