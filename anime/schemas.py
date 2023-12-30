from marshmallow import Schema, fields

AnimeSchema = Schema.from_dict(
    {
        "anime_id": fields.Str(),
        "name": fields.Str(),
        "genre": fields.Str(),
        "type": fields.Str(),
        "episodes": fields.Str(),
        "rating": fields.Float(),
        "members": fields.Integer(),
    }
)
