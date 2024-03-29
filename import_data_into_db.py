import csv

from sqlalchemy.orm import sessionmaker

from anime.models import Anime, engine

Session = sessionmaker(bind=engine)

session = Session()

with open('animes.csv', newline='') as csvfile:

    # Read csv file
    anime_table = csv.DictReader(csvfile)

    for row in anime_table:

        if row['episodes'] == 'Unknown':
            row['episodes'] = None
        else:
            pass

        try:
            row['rating'] = float(row['rating'])
        except ValueError:
            row['rating'] = 0.0

        session.add(Anime(**row))
        session.commit()
