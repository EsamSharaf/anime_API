from flask_jwt_extended import jwt_manager
from flask_sqlalchemy import SQLAlchemy

from anime.models import Base

jwt = jwt_manager.JWTManager()
db = SQLAlchemy(model_class=Base)