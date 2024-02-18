from flask import Blueprint, abort, jsonify, request
from marshmallow.exceptions import ValidationError
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

@animes_bp.route('/api/v1/animes/<int:id>', methods=['PUT', 'PATCH'])
def update_anime(id: int):
    """Route updates attribute(s) of single anime in DB

    :param id: Anime ID
    :type id: str
    :return: Updated anime record
    :rtype: AnimeSchema
    """

    if request.method == 'PUT':
        anime_schema = AnimeSchema()
    else:
        anime_schema = AnimeSchema(partial=True)

    try:
        entry_dict = anime_schema.loads(request.data)
    except ValidationError as e:
        return {"error": e.messages}, 400

    # Function to convert ORM obj to dictionary
    row2dict = lambda r: {
        c.name: str(getattr(r, c.name)) for c in r.__table__.columns}

    db_anime = db.session.query(Anime).filter(Anime.anime_id == id)
    if db_anime.first() is not None:
        db_anime_dict = row2dict(db_anime.first())
    else:
        abort(404)  # if anime id not exist

    for value in entry_dict:
        if entry_dict[value] is not None:
            db_anime_dict[value] = entry_dict[value]

    db_anime.update(db_anime_dict)
    db.session.commit()

    return anime_schema.dump(db_anime_dict)


@animes_bp.route('/api/v1/animes/<int:id>', methods=['DELETE'])
def anime_delete(id: int):
    """Route deletes a single anime in DB if exits or aborts
    if it does not exits

    :param id: Anime id
    :type id: int
    :return: empty string with HTTP status 204 (No Content)
    :rtype: 204 response
    """

    anime = db.get_or_404(Anime, id)
    db.session.delete(anime)
    db.session.commit()

    return '', 204
