import csv

from sqlalchemy.orm import sessionmaker

from models import Anime, engine

Session = sessionmaker(bind=engine)

session = Session()

empty_field_val = {
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

    for row in anime_table:
        for col in row:
            if row[col] == "":

                row[col] = empty_field_val[col]

        session.add(Anime(**row))

        session.commit()
