from flask import Blueprint, jsonify
from sqlalchemy import desc

from app import animes_tab, db

animes_bp = Blueprint('animes', __name__,)

@animes_bp.route('/api/v1/animes/')
def animes():

    query = db.session.execute(
                db.select(animes_tab).order_by(desc(animes_tab.c.rating)))

    animes_rows = query.mappings().fetchall()

    animes_dicts = [dict(zip(row.keys(), row.values())) for row in animes_rows]

    return jsonify(animes_dicts)
