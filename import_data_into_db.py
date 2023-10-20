import pandas as pd
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

# read .csv file
df = pd.read_csv("animes.csv")


def populatDB():
    """Funtion to populate sqlite DB with animes entries from csv file"""

    for row in df.itertuples():
        session.add(
            Animes(
                row.anime_id,
                row.name,
                row.genre,
                row.type,
                row.episodes,
                row.rating,
                row.members,
            )
        )

        session.commit()
