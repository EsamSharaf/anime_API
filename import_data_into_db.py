import csv

from sqlalchemy.orm import sessionmaker

from models import Anime, engine

Session = sessionmaker(bind=engine)

session = Session()

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

        session.add(Anime(**row))

        session.commit()
