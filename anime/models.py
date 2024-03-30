from sqlalchemy import Column, Float, Integer, String, create_engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Anime(Base):
    """Model class returns a table object of a name animes

    :param anime_id: Anime ID
    :type anime_id: int
    :param name: Anime name
    :type name: str
    :param genre: Anime genre
    :type genre: str
    :param type: Anime type
    :type type: str
    :param episodes: Episode number
    :type episodes: int
    :param rating: Episode rating
    :type rating: float
    :param members: Anime members
    :type members: int
    """

    __tablename__ = "animes"

    anime_id = Column("anime_id", Integer, primary_key=True)
    name = Column("name", String)
    genre = Column("genre", String)
    type = Column("type", String)
    episodes = Column("episodes", Integer)
    rating = Column("rating", Float)
    members = Column("members", Integer)

    def __init__(self, anime_id, name, genre, type, episodes, rating, members):
        """
        Constructor method
        """
        self.anime_id = anime_id
        self.name = name
        self.genre = genre
        self.type = type
        self.episodes = episodes
        self.rating = rating
        self.members = members

    def as_dict(self):
        return {column.name: getattr(self, column.name) for column in
                self.__table__.columns}


class User(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(64), unique=True, index=True)
    password = Column(String(128))


engine = create_engine("sqlite:///./instance/animeDB")

Base.metadata.create_all(bind=engine)
