from flask import Blueprint, jsonify
from sqlalchemy import desc


def config_routes(db):

    animes_bp = Blueprint('animes', __name__,)

    @animes_bp.route('/api/v1/animes/')
    def animes():

        animes_tab = db.Table('animes', db.metadata, autoload_with=db.engine)
        query = db.session.execute(
            db.select(animes_tab).order_by(desc(animes_tab.c.rating)))
        animes_rows = query.mappings().fetchall()
        animes_dicts = [dict(zip(row.keys(), row.values())) for row in animes_rows]

        return jsonify(animes_dicts)

    return animes_bp
