from flask_login import login_url
from app import myapp_obj
from flask import render_template, Flask, flash, redirect
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm

name = "Tejas"

@myapp_obj.route("/", methods=('GET', 'POST'))
def home():
	return render_template('home.html')

@myapp_obj.route("/login", methods=('GET', 'POST'))
def loginPage():
    return render_template('home.html')
  
@myapp_obj.route("/create", methods=('GET', 'POST'))
def createAccount():
	return render_template('createAcc.html')

@myapp_obj.route("/profile", methods=('GET', 'POST'))
def profile():
    return render_template('profilepage.html', name = name)