from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

# create the app
app = Flask(__name__)

# configure the SQLite database for testing
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test_animeDB"

# initialize the app with the extension
db.init_app(app)

with app.app_context():
    db.reflect()
    animes_tab = db.Table('animes', db.metadata, autoload_with=db.engine)

from views import animes_bp

app.register_blueprint(animes_bp)


def test_animes_route():
    client = app.test_client()
    response = client.get('/api/v1/animes/')
    assert response.status_code == 200
