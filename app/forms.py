import email
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DecimalField, IntegerField
from wtforms.validators import InputRequired, Length, EqualTo, ValidationError, DataRequired, Email
from app.models import User

#Sign Up form
class RegistrationForm(FlaskForm):
	
	#function to check if username already exists
	def validate_username(self, username_to_check):
		user = User.query.filter_by(username = username_to_check.data).first()
		if user:
			raise ValidationError('Username already exists! Please try different username.')

	#function to check if email already exists
	def validate_email_address(self, email_address_to_check):
		email_address = User.query.filter_by(email_address = email_address_to_check.data).first()
		if email_address:
			raise ValidationError('Email address already exists! Please try different email.')

	#Form fields with validators to check for empty input, really short or long length, no empty field in the form
	username = StringField(label='Username', validators=[InputRequired(message="Username required"), Length(min=4, max=32, message="Username must be between 4 and 32 characters"), DataRequired()])
	email_address=StringField(label='Email', validators=[Email(message="Invalid Email address"), DataRequired()])
	password1 = PasswordField(label='Password', validators=[InputRequired(message="Password required"), Length(min=4, max=32, message="Password must be between 4 and 32 characters"), DataRequired()])
	password2 = PasswordField(label='Confirm Password', validators=[InputRequired(message="Password required"), EqualTo('password1', message="Passwords must match"), DataRequired()])
	submit = SubmitField(label='Submit')

#Lising form
class ListItemForm(FlaskForm):
	name = StringField(label='Product Name', validators=[InputRequired(message="Product name is required!"), Length(min=4, max=32, message="Product name must be between 4 and 32 characters"), DataRequired()])
	description = StringField(label='Product Description', validators=[InputRequired(message="Product description is required!"), Length(min=4, max=128, message="Product description must be between 4 and 128 characters"), DataRequired()])
	price = IntegerField(label='Product Price', validators=[InputRequired(message='Product price is required!'),])
	submit = SubmitField('List Product!')		#Submit button for listing


#Login form
class LoginForm(FlaskForm):
	username = StringField('Username', validators=[InputRequired(message="Username required"), DataRequired()])
	password = PasswordField('Password', validators=[InputRequired(message="Password required"), DataRequired()])
	submit = SubmitField('Log In')

#Purchasing form
class PurchaseItemForm(FlaskForm):
	submit = SubmitField(label='Purchase Product!')	#Submit button for purchasing

#Selling form
class SellItemForm(FlaskForm):
	submit = SubmitField(label='Sell Product!')		#Submit button for selling

#Searching form
class SearchForm(FlaskForm):
	searched = StringField('Searched', validators=[DataRequired()])
	submit = SubmitField('Submit')					#Submit button for searching

#Password form fields with validators to check for empty input, really short or long length, no empty field in the form
#Change Password form
class PasswordForm(FlaskForm):
	currentpass = PasswordField(label='Enter Current Password', validators=[InputRequired(message="Password required"), DataRequired()]) 
	newpass = PasswordField(label='Enter New Password', validators=[InputRequired(message="Password required"), Length(min=4, max=32, message="Password must be between 4 and 32 characters"), DataRequired()])
	submit = SubmitField(label='Submit')
