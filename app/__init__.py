from flask_sqlalchemy import SQLAlchemy
from flask import Flask

myapp_obj = Flask(__name__);
#db = SQLAlchemy(myapp_obj);



myapp_obj.config.from_mapping(SECRET_KEY = 'hr738rgh3q2[qp[2dq//2dqjd9q8/2jd2dm2d')


from app import routes, models, myapp_obj
