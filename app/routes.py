from crypt import methods
from app.forms import RegistrationForm, LoginForm, PurchaseItemForm, SellItemForm, SearchItemForm
from flask import render_template, redirect, url_for, request, flash
from app import myapp_obj, db
from app.models import Item, User, Cart
from flask_login import login_user, logout_user, login_required, current_user

@myapp_obj.route("/", methods=['GET', 'POST'])
def home():
	return render_template('home.html', title='Home')

#Log In page
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

#Log out 
@myapp_obj.route('/logout')
def logoutPage():
	logout_user()
	flash("You have been logged out!", category='info')
	return redirect(url_for("home"))

#Market Page
@myapp_obj.route("/market", methods=['GET', 'POST'])
@login_required
def market():
	purchase_form = PurchaseItemForm()
	selling_form = SellItemForm()
	if request.method == 'POST':
    	#purchase Item logic
		if request.form.get('addtocartform') == 'Add to Cart':
			flash('Item Added to Cart!', category='success')
			#flash(request.form.get('userid2'))
			userid2 = request.form.get('userid2')
			itemid2 = request.form.get('itemid2')
			#flash(request.form.get('itemid2'))
			cartitem = Cart(userid=userid2, itemid=itemid2)
			db.session.add(cartitem)
			db.session.commit()

		purchased_item = request.form.get('purchased_item')
		p_item_obj = Item.query.filter_by(name = purchased_item).first()
		if p_item_obj:
			if current_user.can_purchase(p_item_obj):
				p_item_obj.buy(current_user)
				flash(f"Congratulations! You purchased {p_item_obj.name}", category='success')
			else:
				flash(f"Not enough money to purchase {p_item_obj.name}", category='danger')
		#sell Item logic
		sold_item = request.form.get('sold_item')
		s_item_obj = Item.query.filter_by(name = sold_item).first()
		if s_item_obj:
			if current_user.can_sell(s_item_obj):
				s_item_obj.sell(current_user)
				flash(f"Congratulations! You sold {s_item_obj.name} back to market!", category='success')
			else:
				flash(f"Something went wrong with selling {s_item_obj.name}", category="danger")
		return redirect(url_for('market'))		

	if request.method == 'GET':
		items = Item.query.filter_by(owner=None)
		owned_items = Item.query.filter_by(owner = current_user.id)
		return render_template('market.html', items=items, purchase_form=purchase_form, selling_form = selling_form, title='Market', owned_items = owned_items)

	


#Sign Up page  
@myapp_obj.route("/signup", methods=['GET', 'POST'])
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

#Profile Page
@myapp_obj.route("/profilepage", methods=['GET', 'POST'])
def profile():
    return render_template('profilepage.html', title='My Profile')

#CART page
@myapp_obj.route("/cart", methods=['GET', 'POST'])
@login_required
def cart():
	userid2 = request.form.get('userid2')
	itemdetails = list()

	
	for eachitem in db.session.query(Cart.id,Item.id,Item.name,Item.price).filter(Item.id == Cart.itemid, Cart.userid == userid2).all():
		itemdetails.append(eachitem)

	if request.method == 'POST':
		if request.form.get('removefromcartform') == 'Remove from Cart':
			#flash('Item Removed from Cart!', category='success')
            #flash(request.form.get('userid2'))
			#userid2 = request.form.get('userid2')
			#itemid2 = request.form.get('itemid2')
			cartid2 = request.form.get('cartid2')

			i = Cart.query.filter_by(id = cartid2).first()
			db.session.delete(i)
			db.session.commit()
			return redirect(url_for('market'))
		else:
			None# unknown
	elif request.method == 'GET':
		return render_template('cart.html', itemdetails = itemdetails, title='My Cart')
	return render_template('cart.html', itemdetails = itemdetails, title='My Cart', len = len(itemdetails) )


#pass stuff to navbar
@myapp_obj.context_processor
def base():
	form = SearchItemForm()
	return dict(form=form)

#Search Page
@myapp_obj.route("/search", methods=['POST'])
def search():
	form = SearchItemForm()
	if form.validate_on_submit():
		db.searched = form.searched.data
		return render_template("search.html", form = form, searched = db.searched)

