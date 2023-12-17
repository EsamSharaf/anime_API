from flask import Flask
from conduit.extensions import db
from conduit.views import animes_bp
from conduit.settings import DevConfig


def create_app(config_object=DevConfig):
    """An application factory, as explained here:
    http://flask.pocoo.org/docs/patterns/appfactories/.

    :param configconfig_object_object: The configuration object to use.
    """
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    register_blueprints(app)
    # register_errorhandlers(app)
    # register_shellcontext(app)
    # register_commands(app)
    return app

def register_extensions(app):
    """Register Flask extensions."""

    db.init_app(app)
    with app.app_context():
        db.reflect()

def register_blueprints(app):
    """Register Flask blueprints."""

    # origins = app.config.get('CORS_ORIGIN_WHITELIST', '*')
    # cors.init_app(user.views.blueprint, origins=origins)
    # cors.init_app(profile.views.blueprint, origins=origins)
    # cors.init_app(articles.views.blueprint, origins=origins)

    app.register_blueprint(animes_bp)
    # app.register_blueprint(profile.views.blueprint)
    # app.register_blueprint(articles.views.blueprint)

############ Old APP ###################################################

# # create the app
# app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///animeDB"

# # initialize the app with the extension
# db.init_app(app)

# with app.app_context():
#     db.reflect()

#     animes_bp = config_routes(db)
#     app.register_blueprint(animes_bp)
