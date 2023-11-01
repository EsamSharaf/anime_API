from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase


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
    db.Model.metadata.reflect(db.engine)


class Anime(db.Model):
    __table__ = db.Model.metadata.tables['anime']
