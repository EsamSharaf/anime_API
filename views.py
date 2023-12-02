from flask import Blueprint, jsonify
from sqlalchemy import desc


def config_routes(db):

    animes_bp = Blueprint('animes', __name__,)

    @animes_bp.route('/api/v1/animes/')
    def animes():
        """route responds with animes table's rows sorted by
        rating attribute in descending order

        :return: a list of table rows (objects)
        :rtype: list of JSON-formatted objects
        """

        animes_tab = db.Table('animes', db.metadata, autoload_with=db.engine)
        query = db.session.execute(
            db.select(animes_tab).order_by(desc(animes_tab.c.rating)))
        animes_rows = query.mappings().fetchall()
        animes_dicts = [dict(zip(row.keys(), row.values())) for row in animes_rows]

        return jsonify(animes_dicts)

    @animes_bp.route('/api/v1/anime/<string:name>')
    def get_anime_by_name(name: str):
        """route responds with a single row from animes table which matches
        its name the name argument or "anime not found" string message

        :param name: anime name
        :type name: str
        :return: a JSON object
        :rtype: JSON response object
        """

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
