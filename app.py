from flask import Flask
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


@app.route('/list')
def list():
    animes = db.session.execute(db.select(Anime).order_by(Anime.rating)
                                ).scalars()
    print(animes)
    return [anime.to_json() for anime in animes]
