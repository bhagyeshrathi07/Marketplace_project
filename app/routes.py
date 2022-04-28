from app.forms import *
from flask_login import login_url
from app import myapp_obj
from flask import render_template, Flask, flash, redirect, url_for
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm

from wtform_fields import *
from models import *

name = "Tejas"

@myapp_obj.route("/", methods=('GET', 'POST'))
def home():
	return render_template('home.html')

@myapp_obj.route("/market.html") #, methods=('GET', 'POST'))
def market():
    items = [
        {'name': 'iphone 12 Pro', 'description': '256GB', 'price': 1000},
		{'name': 'macbook pro', 'description': '512 GB, space gray', 'price': 1600},
        {'name': 'ipad pro', 'description': '256 GB WiFi', 'price': 850}]
    return render_template('market.html', items=items)

@myapp_obj.route("/login.html", methods=('GET', 'POST'))
def loginPage():
	login = LoginForm()

	if login.validate_on_submit():
		return "Logged in, finally!"

    	return render_template('login.html', form=login)

'''@myapp_obj.route("/createAcc.html", methods=('GET', 'POST'))
def createAccount():
	register = RegistrationForm()

	if register.validate_on_submit():
		username = register.username.data
		password = register.password.data

		user = User(username=username, password=password)
		db.session.add(user)
		db.session.commit()

		return redirect(url_for('login')

	return render_template('createAcc.html', form=register)'''

@myapp_obj.route("/profilepage.html", methods=('GET', 'POST'))
def profile():
    return render_template('profilepage.html', name = name)

@myapp_obj.route("/cart.html", methods=('GET', 'POST'))
def cart():
    return render_template('cart.html')
