from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

import os

basedir = os.path.abspath(os.path.dirname(__file__))

myapp_obj = Flask(__name__);
db = SQLAlchemy(myapp_obj);


myapp_obj.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
myapp_obj.config['SECRET_KEY'] = '032acac8f265a4205baaa601'      #DO NOT CHANGE THIS HEXADECIMAL SECRET_KEY

from app import routes
