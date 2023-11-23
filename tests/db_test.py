from flask_sqlalchemy import SQLAlchemy

from models import Base

db = SQLAlchemy(model_class=Base)
