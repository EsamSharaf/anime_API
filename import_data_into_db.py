import csv

from sqlalchemy import Column, Float, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Animes(Base):

    __tablename__ = "animes"

    anime_id = Column("anime_id", Integer, primary_key=True)
    name = Column("name", String)
    genre = Column("genre", String)
    type = Column("type", String)
    episodes = Column("episodes", Integer)
    rating = Column("rating", Float)
    members = Column("members", Integer)

    def __init__(self, anime_id, name, genre, type, episodes, rating, members):
        self.anime_id = anime_id
        self.name = name
        self.genre = genre
        self.type = type
        self.episodes = episodes
        self.rating = rating
        self.members = members


engine = create_engine("sqlite:///animDB")

Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)

session = Session()


def populate_db(row):
    """Funtion to populate sqlite DB with animes entries from csv file"""

    session.add(
            Animes(
                row['anime_id'],
                row['name'],
                row['genre'],
                row['type'],
                row['episodes'],
                row['rating'],
                row['members'],
            )
        )

    session.commit()

# Dictionary with values to fill empty fields
default = {
    'anime_id': 'unkownn',
    'name': 'unkown',
    'genre': 'unkown',
    'type': 'unkown',
    'episodes': -1,
    'rating': -1,
    'members': -1,
}

with open('animes.csv', newline='') as csvfile:

    # Read csv file
    anime_table = csv.DictReader(csvfile)

    # Populate the DB row by row
    for row in anime_table:
        for col in row:
            if row[col] == "":

                row[col] = default[col]

        populate_db(row)
