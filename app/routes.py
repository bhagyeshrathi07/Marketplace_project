from app.forms import RegistrationForm, LoginForm
from flask import render_template, redirect, url_for, request, flash
from app import myapp_obj, db
from app.models import Item, User, Cart
from flask_login import login_user, logout_user, login_required

@myapp_obj.route("/", methods=['GET', 'POST'])
def home():
	return render_template('home.html', title='Home')

@myapp_obj.route("/login", methods=['GET', 'POST'])
def loginPage():
	form = LoginForm()
	if form.validate_on_submit():
		attempted_user = User.query.filter_by(username=form.username.data).first()
		if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):
			login_user(attempted_user)
			flash(f'Success logging in, Logged in as: {attempted_user.username}', category='success')
			return redirect(url_for('market'))
		else:
			flash('Username or Password does not match! Please try again', category='danger')
	return render_template('login.html', title='Login', form=form) 		

@myapp_obj.route('/logout')
def logoutPage():
	logout_user()
	flash("You have been logged out!", category='info')
	return redirect(url_for("home"))


@myapp_obj.route("/market", methods=['GET', 'POST'])
@login_required
def market():
    items = Item.query.all()
    # username2 = form.username.data
    # useridtemp = User.query.filter_by(id = username2).all()
    # for i in items.id
    #itemidtemp = 
    if request.method == 'POST':
        if request.form.get('addtocartform') == 'Add to Cart':
            flash('Item Added to Cart!', category='success')
            flash(request.form.get('userid2'))
            userid2 = request.form.get('userid2')
            itemid2 = request.form.get('itemid2')
            flash(request.form.get('itemid2'))
            cartitem = Cart(userid=userid2, itemid=itemid2)
            db.session.add(cartitem)
            db.session.commit()

        else:
            flash('There was an error, please try again', category='danger')# unknown
    elif request.method == 'GET':
        return render_template('market.html', items=items, title='Market')
    return render_template('market.html', items=items, title='Market')
<<<<<<< HEAD

@myapp_obj.route("/signup", methods=('GET', 'POST'))
=======
  
@myapp_obj.route("/signup", methods=['GET', 'POST'])
>>>>>>> main
def signupPage():
	form = RegistrationForm()
	if form.validate_on_submit():
		user_to_create = User(username=form.username.data, email_address=form.email_address.data, password=form.password1.data)
		db.session.add(user_to_create)
		db.session.commit()
		login_user(user_to_create)
		flash(f'Account created successfully! You are now logged in as {user_to_create.username}', category='success')
		return redirect(url_for('market'))
	if form.errors != {}: #If there are no errors from the validations
		for err_msg in form.errors.values():
				flash(f'There was an error with creating a user: {err_msg}', category='danger')

	return render_template('signup.html', form=form, title='Signup')

@myapp_obj.route("/profilepage", methods=['GET', 'POST'])
def profile():
    return render_template('profilepage.html', title='My Profile')

@myapp_obj.route("/cart", methods=['GET', 'POST'])
def cart():
	cart = Cart.query.filter_by(userid = 1).all()
	itemdetails = list()
	for id2 in cart:
		for eachitem in Item.query.filter_by(id = id2.itemid).all():	
			itemdetails.append(eachitem)
	return render_template('cart.html', itemdetails = itemdetails, title='My Cart', len = len(itemdetails) )

#useritems=cart,
	#query = dbsession.query(MyTable).filter(MyTable.name==u'john')
#rows = query.statement.execute().fetchall()
#for row in rows:
 #   print row

