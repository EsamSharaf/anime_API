from marshmallow import Schema, fields

AnimeSchema = Schema.from_dict(
    {
        "anime_id": fields.Int(),
        "name": fields.Str(),
        "genre": fields.Str(),
        "type": fields.Str(),
        "episodes": fields.Str(),
        "rating": fields.Float(),
        "members": fields.Int(),
    }
)
