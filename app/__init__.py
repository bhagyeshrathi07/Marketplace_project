from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(myapp_obj)

from app import routes, models
