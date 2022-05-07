from app.forms import RegistrationForm, LoginForm, PurchaseItemForm, SellItemForm, SearchForm, PasswordForm
from flask import render_template, redirect, url_for, request, flash
from app import myapp_obj, db
from app.models import Item, User, Cart
from flask_login import login_user, logout_user, login_required, current_user

@myapp_obj.route("/", methods=['GET', 'POST'])
def home():
	return render_template('home.html', title='Home')

@myapp_obj.route("/login", methods=['GET', 'POST'])
def loginPage():
	form = LoginForm()
	if form.validate_on_submit():	#check if submit is clicked
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
	purchase_form = PurchaseItemForm()  # purchase form from forms.py
	selling_form = SellItemForm()		# sell form from forms.py
	if request.method == 'POST':
    	#add to cart logic
		if request.form.get('addtocartform') == 'Add to Cart':
			flash('Item Added to Cart!', category='success')
			#flash(request.form.get('userid2'))
			userid2 = request.form.get('userid2')
			itemid2 = request.form.get('itemid2')
			#flash(request.form.get('itemid2'))
			cartitem = Cart(userid=userid2, itemid=itemid2)
			db.session.add(cartitem)
			db.session.commit()
		
		#purchase Item logic
		purchased_item = request.form.get('purchased_item')
		p_item_obj = Item.query.filter_by(name = purchased_item).first()  
		if p_item_obj:	#check if item exists in market
			if current_user.can_purchase(p_item_obj): 	#check if current logged in user can buy it
				p_item_obj.buy(current_user)	#if he can user buys object
				flash(f"Congratulations! You purchased {p_item_obj.name}", category='success')	#flash success message
			else:
				flash(f"Not enough money to purchase {p_item_obj.name}", category='danger')	#else flash error message
				
		#sell Item logic
		sold_item = request.form.get('sold_item')
		s_item_obj = Item.query.filter_by(name = sold_item).first()
		if s_item_obj: #check if item owned by user
			if current_user.can_sell(s_item_obj):	#check if current logged in user can sell it
				s_item_obj.sell(current_user)	#if he can sell it
				flash(f"Congratulations! You sold {s_item_obj.name} back to market!", category='success') #show success message
			else:
				flash(f"Something went wrong with selling {s_item_obj.name}", category="danger") #else show error message and redirect to market
		return redirect(url_for('market'))		

	if request.method == 'GET':
		items = Item.query.filter_by(owner=None) #query all the items that are not yet sold
		owned_items = Item.query.filter_by(owner = current_user.id)	#query all the items owned by current logged in user
		return render_template('market.html', items=items, purchase_form=purchase_form, selling_form = selling_form, title='Market', owned_items = owned_items)

	


  
@myapp_obj.route("/signup", methods=['GET', 'POST'])
def signupPage():
	form = RegistrationForm()  #signup form from forms.py
	if form.validate_on_submit():
		user_to_create = User(username=form.username.data, email_address=form.email_address.data, password=form.password1.data)	#get data from the form user filled
		db.session.add(user_to_create)
		db.session.commit()	#add it to database
		login_user(user_to_create)	#login the user if signup is successfull
		flash(f'Account created successfully! You are now logged in as {user_to_create.username}', category='success')	#flash success message
		return redirect(url_for('market'))	#redirect to market after logging in
	if form.errors != {}: #If there are errors in signing up
		for err_msg in form.errors.values():
				flash(f'There was an error with creating a user: {err_msg}', category='danger') #flash appropriate error message

	return render_template('signup.html', form=form, title='Signup')



@myapp_obj.route("/profilepage", methods=['GET', 'POST'])
def profile():
	if request.method == 'POST':
		if request.form.get('deleteprofile') == 'Delete Profile':
			userid2 = request.form.get('userid2')
			u = User.query.filter_by(id = userid2).first()
			usercart = db.session.query(Cart).filter(Cart.userid == userid2).delete()
			#db.session.delete(usercart)
			db.session.delete(u)
			db.session.commit()
			flash('Profile Deleted!', category='success')
			return redirect(url_for('logoutPage'))
		if request.form.get('changepassword') == 'Change Password':
			return redirect(url_for('changepassword'))
		else:
			None# unknown
	elif request.method == 'GET':
		return render_template('profilepage.html', title='My Profile')



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

			c = Cart.query.filter_by(id = cartid2).first()
			db.session.delete(c)
			db.session.commit()
			return redirect(url_for('market'))
		else:
			None# unknown
	elif request.method == 'GET':
		return render_template('cart.html', itemdetails = itemdetails, title='My Cart')
	return render_template('cart.html', itemdetails = itemdetails, title='My Cart', len = len(itemdetails) )


@myapp_obj.context_processor
def base():
	form = SearchForm()
	return dict(form=form)

@myapp_obj.route('/search', methods=["POST"])
def search():
	form = SearchForm()
	searcheditems = Item.query
	
	
	#if form.validate_on_submit():
		#item_searched = form.searched.data
	item_searched = request.form.get('searched')
		#flash(item_searched)

		#searcheditems = db.session.query(Item.name, Item.price).filter(Item.name == item_searched).all()
	searcheditems = db.session.query(Item.name, Item.price, Item.id, Item.description).filter(Item.name.like('%' + item_searched + '%')).all()
		#searcheditems = searcheditems.order_by(Item.name).all
		#flash(searcheditems)
	if request.form.get('addtocartform') == 'Add to Cart':
		flash('Item Added to Cart!', category='success')
		#flash(request.form.get('userid2'))
		userid2 = request.form.get('userid2')
		itemid2 = request.form.get('itemid2')
		#flash(request.form.get('itemid2'))
		cartitem = Cart(userid=userid2, itemid=itemid2)
		db.session.add(cartitem)
		db.session.commit()
			
		
	return render_template("search.html", form=form, item_searched = item_searched, searcheditems = searcheditems)
	#return render_template("search.html", form=form)



@myapp_obj.route('/changepassword', methods=["GET", "POST"])
def changepassword():
	form = PasswordForm()
	if form.validate_on_submit():	#check if submit is clicked
		currentpass = form.currentpass.data
		newpass = form.newpass.data 
		userid2 = request.form.get('userid2')
		u = User.query.filter_by(id = userid2).first()
		if u.check_password_correction(currentpass):
			u.password = form.newpass.data
			db.session.add(u)
			db.session.commit()
			flash("Your Password Has Been Changed", category='success')
			return render_template("changepassword.html", form=form)
		else: 
			flash("Incorrect Password", category='danger')
			return render_template("changepassword.html", form=form)
	return render_template("changepassword.html", form=form)