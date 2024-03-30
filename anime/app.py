from flask import Flask, jsonify
from marshmallow import ValidationError

from anime.extensions import db, jwt
from anime.settings import DevConfig
from anime.views import animes_bp


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
    register_error_handlers(app)

    return app

def register_extensions(app):
    """Register Flask extensions."""

    db.init_app(app)
    with app.app_context():
        db.reflect()
    jwt.init_app(app)

def register_blueprints(app):
    """Register Flask blueprints."""

    app.register_blueprint(animes_bp)

def register_error_handlers(app):
    """Register Flask error handler on app level."""

    @app.errorhandler(ValidationError)
    def validiation_error(e):
        return jsonify({"message": str(e)}), 400
