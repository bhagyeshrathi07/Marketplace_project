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

@myapp_obj.route("/market") #, methods=('GET', 'POST'))
def market():
	#sample Items in market
	items = [
		{'id': 1, 'name': 'iphone7', 'barcode': '893212299897', 'price': 500}
		{'id': 2, 'name': 'macbook air', 'barcode': '985792304857', 'price': 1500}
		{'id': 3, 'name': 'Ipad pro', 'barcode': '856342895798', 'price': 899}
	]
	return render_template('market.html', items = items)

@myapp_obj.route("/login", methods=('GET', 'POST'))
def loginPage():
    return render_template('login.html')
  
@myapp_obj.route("/signup", methods=('GET', 'POST'))
def createAccount():
	register = RegistrationForm()

	"""if registration.validate_on_submit():
		username = register.username.data
		password = register.password.data

		user = User(username=username, password=password)
		db.session.add(user)
		db.session.commit()

		return"""
	return render_template('createAcc.html', form=register)

@myapp_obj.route("/profile", methods=('GET', 'POST'))
def profile():
    return render_template('profilepage.html', name = name)

