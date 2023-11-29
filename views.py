from flask import Blueprint, jsonify
from sqlalchemy import desc


def config_routes(db):

    animes_bp = Blueprint('animes', __name__,)

    @animes_bp.route('/api/v1/animes/')
    def animes():
        """Route returns anime objects in DB listed by rating attribute"""

        animes_tab = db.Table('animes', db.metadata, autoload_with=db.engine)
        query = db.session.execute(
            db.select(animes_tab).order_by(desc(animes_tab.c.rating)))
        animes_rows = query.mappings().fetchall()
        animes_dicts = [dict(zip(row.keys(), row.values())) for row in animes_rows]

        return jsonify(animes_dicts)

    @animes_bp.route('/api/v1/anime/<string:name>')
    def get_anime_by_name(name: str):
        """Route retrun single anime details from DB"""

        animes_tab = db.Table('animes', db.metadata, autoload_with=db.engine)
        query = db.session.execute(db.select(animes_tab).filter_by(name=name))
        row = query.first()
        try:
            anime_dict = row._asdict()

        except AttributeError:
            return "anime not found"
        else:
            return jsonify(anime_dict)

    return animes_bp
