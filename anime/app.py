from flask import Flask

from anime.extensions import db
from anime.settings import DevConfig
from anime.views import animes_bp

from .error_handlers import RecordIdExist, handle_record_exist


def create_app(config_object=DevConfig):
    """Application factory

    :param config_object: The configuration object to use.
    :type config_object: Config class object
    :return: Flask app
    :rtype: Flask app object
    """
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    register_blueprints(app)
    app.register_error_handler(RecordIdExist, handle_record_exist)
    return app

def register_extensions(app):
    """Register Flask extensions."""

    db.init_app(app)
    with app.app_context():
        db.reflect()

def register_blueprints(app):
    """Register Flask blueprints."""

    app.register_blueprint(animes_bp)
