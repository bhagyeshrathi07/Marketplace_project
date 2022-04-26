from flask_sqlalchemy import SQLAlchemy
from app import myapp_obj

db = SQLAlchemy(myapp_obj)

from app import routes, models
