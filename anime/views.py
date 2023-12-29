from flask import Blueprint, abort, jsonify
from sqlalchemy import desc

from anime.app import db
from anime.models import Anime

animes_tab = Anime.__table__

animes_bp = Blueprint('animes', __name__,)

@animes_bp.route('/api/v1/animes/', methods=['GET'])
def animes():
    """route responds with animes table's rows sorted by
    rating attribute in descending order

    :return: a list of table rows (objects)
    :rtype: list of JSON-formatted objects
    """

    query = db.session.execute(
        db.select(animes_tab).order_by(desc(animes_tab.c.rating)))
    animes_rows = query.all()
    animes_dicts = [row._asdict() for row in animes_rows]

    return jsonify(animes_dicts)

@animes_bp.route('/api/v1/anime/<string:name>', methods=['GET'])
def get_anime_by_name(name: str):
    """route responds with a single row from animes table which matches
    its name the name argument or "anime not found" string message

    :param name: anime name
    :type name: str
    :raises AttributeError: handles when row is None
    :return: a JSON object
    :rtype: JSON response object
    """

    query = db.session.execute(db.select(animes_tab).filter_by(name=name))
    row = query.first()
    if row is not None:
        anime_dict = row._asdict()
        return jsonify(anime_dict)
    else:
        abort(404)
