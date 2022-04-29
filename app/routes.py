
from app.forms import RegistrationForm
from flask import render_template
from app import myapp_obj, db
from app.models import Item, User


@myapp_obj.route("/", methods=('GET', 'POST'))
def home():
	return render_template('home.html', title='Home')

@myapp_obj.route("/login", methods=('GET', 'POST'))
def loginPage():
    return render_template('login.html', title='Login')

@myapp_obj.route("/market", methods=('GET', 'POST'))
def market():
    items = Item.query.all()
    return render_template('market.html', items=items, title='Market')
  
@myapp_obj.route("/signup", methods=('GET', 'POST'))
def signupPage():
	form = RegistrationForm()
	return render_template('signup.html', form=form, title='Signup')

@myapp_obj.route("/profilepage", methods=('GET', 'POST'))
def profile():
    return render_template('profilepage.html', title='My Profile')

@myapp_obj.route("/cart", methods=('GET', 'POST'))
def cart():
    return render_template('cart.html', title= 'Cart')

