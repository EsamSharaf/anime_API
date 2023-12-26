from flask_sqlalchemy import SQLAlchemy
from conduit.models import Base


db = SQLAlchemy(model_class=Base)
