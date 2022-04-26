from flask_login import login_url
from app import myapp_obj
from flask import render_template

@myapp_obj.route("/login")
def loginPage():
    return render_template('home.html')

@myapp_obj.route("/create")
def createAccount():
	register = RegistrationForm()

	if registration.validate_on_submit():
		username = register.username.data
		password = register.password.data

		user = User(username=username, password=password)
		db.session.add(user)
		db.session.commit()

		return

	return render_template('createAcc.html', form=register)

@myapp_obj.route("/profile")
def profile():
    return render_template('profilepage.html')
