
from app.forms import *
from flask import render_template
from app import myapp_obj
from models import Item, User


@myapp_obj.route("/")#, methods=('GET', 'POST'))
def home():
	return render_template('home.html', title='Home')

@myapp_obj.route("/login.html")#, methods=('GET', 'POST'))
def loginPage():
    return render_template('login.html', title='Login')

@myapp_obj.route("/market") #, methods=('GET', 'POST'))
def market():
    items = Item.query.all()
    return render_template('market.html', items=items, title='Market')
  
@myapp_obj.route("/signup", methods=('GET', 'POST'))
def signupPage():
	'''register = RegistrationForm()

	if registration.validate_on_submit():
		username = register.username.data
		password = register.password.data

		user = User(username=username, password=password)
		db.session.add(user)
		db.session.commit()

		return'''
	return render_template('signup.html', title='Signup')

@myapp_obj.route("/profilepage", methods=('GET', 'POST'))
def profile():
    return render_template('profilepage.html', title='My Profile')

@myapp_obj.route("/cart")#, methods=('GET', 'POST'))
def cart():
    return render_template('cart.html', title= 'Cart')

