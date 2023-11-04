from app import Anime, app, db

@app.route('/list')
def list():
    animes = db.session.execute(db.select(Anime).order_by(Anime.rating)
                                ).scalars()

    return [anime.to_json() for anime in animes]
