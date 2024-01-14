from flask import Blueprint, abort, jsonify, request
from sqlalchemy import desc

from anime.app import db
from anime.models import Anime
from anime.schemas import AnimeSchema

animes_tab = Anime.__table__

animes_bp = Blueprint('animes', __name__,)

@animes_bp.route('/api/v1/animes/', methods=['GET'])
def animes():
    """Route returns with animes table's rows sorted by
    rating attribute in descending order

    :return: a list of table rows (objects)
    :rtype: list of JSON-formatted objects
    """

    query = db.session.execute(
        db.select(animes_tab).order_by(desc(animes_tab.c.rating)))
    animes_rows = query.all()
    animes_schema = AnimeSchema(many=True)

    return animes_schema.dump(animes_rows)

@animes_bp.route('/api/v1/anime/<string:name>', methods=['GET'])
def get_anime_by_name(name: str):
    """Route returns with a single row from animes table which matches
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
        anime_schema = AnimeSchema()
        return anime_schema.dump(row)
    else:
        abort(404)


@animes_bp.route('/api/v1/anime-update/<string:name>', methods=['POST'])
def update_anime_field(name: str):
    """Route updates attribute(s) of single anime in DB

    :param name: Anime name to update its attribute(s)
    :type name: str
    :return: Query paremeters
    :rtype: JSON
    """

    try:
        request_data = request.get_json()

        for key, val in request_data.items():
            db.session.query(Anime).filter(Anime.name == name).update(
                {key: val}
            )
            db.session.commit()

        anime = db.session.execute(
                    db.select(animes_tab).filter_by(name=name)).first()
        anime_schema = AnimeSchema()

        return anime_schema.dump(anime)

    except Exception as e:
        return jsonify({"error": "{0}".format(e)})
