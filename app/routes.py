from app.forms import RegistrationForm, LoginForm, PurchaseItemForm, SellItemForm, SearchForm, PasswordForm, ListItemForm
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
		if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data): #if the username and password are correct
			login_user(attempted_user) #then login the user session
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
			userid2 = request.form.get('userid2') #pass the user's id and the id of the item to the form
			itemid2 = request.form.get('itemid2')
			#flash(request.form.get('itemid2'))
			cartitem = Cart(userid=userid2, itemid=itemid2) #create a new item in cart class with these params
			db.session.add(cartitem) #add item to database
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
		if request.form.get('deleteprofile') == 'Delete Profile': #if the delete profile button is clicked
			userid2 = request.form.get('userid2')
			u = User.query.filter_by(id = userid2).first() #filter the User class for wherever the given userid is found
			usercart = db.session.query(Cart).filter(Cart.userid == userid2).delete() #delete the cart for the user
			#db.session.delete(usercart)
			db.session.delete(u) #delete the previously found user
			db.session.commit()
			flash('Profile Deleted!', category='success')
			return redirect(url_for('logoutPage')) #flash and redirect
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
	itemdetails = [] 

	for eachitem in db.session.query(Cart.id,Item.id,Item.name,Item.price).filter(Item.id == Cart.itemid, Cart.userid == userid2).all(): #query for the information of items in users cart
		itemdetails.append(eachitem) #add to the list created above, regular python list would not work.

	if request.method == 'POST':
		if request.form.get('removefromcartform') == 'Remove from Cart': #if remove from cart button is clicked

			cartid2 = request.form.get('cartid2') #get cardid from form

			c = Cart.query.filter_by(id = cartid2).first() #filter the Cart class for that given id
			db.session.delete(c) #and delete that item from that user's cart
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
		currentpass = form.currentpass.data #get data fro both the newpass and the current pass
		newpass = form.newpass.data 
		userid2 = request.form.get('userid2')
		u = User.query.filter_by(id = userid2).first() #find the user object in db
		if u.check_password_correction(currentpass): #check if the users password is the same as the entered "currentpass"
			u.password = form.newpass.data #override the current password in the db with the new one
			db.session.add(u)
			db.session.commit()
			flash("Your Password Has Been Changed", category='success')
			return render_template("changepassword.html", form=form)
		else: 
			flash("Incorrect Password", category='danger')
			return render_template("changepassword.html", form=form)
	return render_template("changepassword.html", form=form)




@myapp_obj.route("/list", methods=['GET', 'POST'])
@login_required
def list():
	form = ListItemForm()		# listing form from forms.py
	if form.validate_on_submit():
		new_item = Item(name = form.name.data, price = form.price.data, description = form.description.data, owner = None)
		db.session.add(new_item)
		db.session.commit()
		flash(f'Product {new_item.name} added to market!', category='success') #flash success message.
		return redirect(url_for('list'))

	if form.errors != {}: #If there are errors in signing up
		for err_msg in form.errors.values():
				flash(f'There was an error with listing the product on market: {err_msg}', category='danger') #flash appropriate error message
	
	return render_template('list_item.html', form = form, title='List')