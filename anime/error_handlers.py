from flask import jsonify


class RecordIdExist(Exception):
    code = 400
    message = "Anime ID already exists in the database." \
        "Ensure input anime ID is unique"
    error = "sqlite3.IntegrityError: UNIQUE constraint failed: animes.anime_id"


def handle_record_exist(e):
    print(e.message)
    return jsonify({"message": e.message, "error": e.error}), e.code
