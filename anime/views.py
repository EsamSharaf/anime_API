from flask import Blueprint, abort, jsonify, request
from flask_jwt_extended import create_access_token, jwt_required
from sqlalchemy import desc
from werkzeug.security import check_password_hash, generate_password_hash

from anime.app import db
from anime.models import Anime, User
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

@animes_bp.route('/api/v1/animes/<int:id>', methods=['Put', 'Patch'])
@jwt_required()
def anime(id: int):
    """Route updates attribute(s) of single anime in DB

    :param name: Anime name to update its attribute(s)
    :type name: str
    :return: Updated anime record
    :rtype: AnimeSchema
    """

    try:
        request_data = request.get_json()
        db.session.query(Anime).filter(Anime.anime_id == id).update(
            {**request_data}
        )
        db.session.commit()

        anime = db.session.execute(
                    db.select(animes_tab).filter_by(anime_id=id)).first()
        anime_schema = AnimeSchema()

        return anime_schema.dump(anime)

    except Exception as e:
        return jsonify({"error": "{0}".format(e)})

@animes_bp.route('/api/v1/animes/<int:id>', methods=['DELETE'])
@jwt_required()
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

@animes_bp.route('/api/v1/register', methods=['POST'])
def register():
    username = request.json.get("username")
    password = request.json.get("password")

    user = User.query.filter_by(username=username).one_or_none()

    if user is not None:
        return jsonify(message='username exists')

    hashed_password = generate_password_hash(password)

    user = User(username=username, password=hashed_password)
    db.session.add(user)
    db.session.commit()
    return jsonify(message='user created')

@animes_bp.route('/api/v1/login', methods=['POST'])
def login():
    username = request.json.get("username")
    password = request.json.get("password")

    user = User.query.filter_by(username=username).one_or_none()

    if user is not None and check_password_hash(user.password, password):
        access_token = create_access_token(identity=username)
        response = jsonify(message='Authorized User', access_token=access_token)
        return response, 200
    else:
        return jsonify(message='login failed'), 401
