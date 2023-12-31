from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

from views import config_routes


class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

# create the app
app = Flask(__name__)

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///animeDB"

# initialize the app with the extension
db.init_app(app)

with app.app_context():
    db.reflect()

    animes_bp = config_routes(db)
    app.register_blueprint(animes_bp)
