from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

import os

basedir = os.path.abspath(os.path.dirname(__file__))


myapp_obj = Flask(__name__);

db = SQLAlchemy(myapp_obj);
myapp_obj.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
#myapp_obj.config.from_mapping(SECRET_KEY = 'hr738rgh3q2[qp[2dq//2dqjd9q8/2jd2dm2d')

from app import routes
