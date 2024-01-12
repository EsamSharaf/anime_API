from flask_sqlalchemy import SQLAlchemy

from anime.models import Base

db = SQLAlchemy(model_class=Base)
