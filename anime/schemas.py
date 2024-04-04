from marshmallow import Schema, fields

AnimeSchema = Schema.from_dict(
    {
        "anime_id": fields.Int(required=True),
        "name": fields.Str(required=True),
        "genre": fields.Str(required=True),
        "type": fields.Str(required=True),
        "episodes": fields.Int(required=True),
        "rating": fields.Float(required=True),
        "members": fields.Int(required=True)
    }
)

UserSchema = Schema.from_dict(
    {
        "username": fields.Str(required=True),
        "password": fields.Str(required=True)
    }
)
