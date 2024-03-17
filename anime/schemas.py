from marshmallow import Schema, fields

AnimeSchema = Schema.from_dict(
    {
        "anime_id": fields.Int(required=True, error_messages={"required": "anime_id is required."}),
        "name": fields.Str(required=True, error_messages={"required": "name is required."}),
        "genre": fields.Str(required=True, error_messages={"required": "genre is required."}),
        "type": fields.Str(required=True, error_messages={"required": "type is required."}),
        "episodes": fields.Int(required=True, error_messages={"required": "episodes is required."}),
        "rating": fields.Float(required=True, error_messages={"required": "rating is required."}),
        "members": fields.Int(required=True, error_messages={"required": "members is required."}),
    }
)
