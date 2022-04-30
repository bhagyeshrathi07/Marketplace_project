
from app.forms import RegistrationForm
from flask import render_template, redirect, url_for
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
  
@myapp_obj.route("/signup", methods=['GET', 'POST'])
def signupPage():
	form = RegistrationForm()
	if form.validate_on_submit():
		user_to_create = User(username=form.username.data, email_address=form.email_address.data, password_hash=form.password1.data)
		db.session.add(user_to_create)
		db.session.commit()
		return redirect(url_for('market'))
	if form.errors != {}: #If there are no errors from the validations
		for err_msg in form.errors.values():
				print(f'There was an error with creating a user: {err_msg}')

	return render_template('signup.html', form=form, title='Signup')

@myapp_obj.route("/profilepage", methods=('GET', 'POST'))
def profile():
    return render_template('profilepage.html', title='My Profile')

@myapp_obj.route("/cart", methods=('GET', 'POST'))
def cart():
	useritems = Item.query.all()
	return render_template('cart.html', items=useritems, title='My Cart')
