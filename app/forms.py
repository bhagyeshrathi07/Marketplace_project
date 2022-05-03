import email
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import InputRequired, Length, EqualTo, ValidationError, DataRequired, Email
from app.models import User


class RegistrationForm(FlaskForm):
	def validate_username(self, username_to_check):
		user = User.query.filter_by(username = username_to_check.data).first()
		if user:
			raise ValidationError('Username already exists! Please try different username.')


	def validate_email_address(self, email_address_to_check):
		email_address = User.query.filter_by(email_address = email_address_to_check.data).first()
		if email_address:
			raise ValidationError('Email address already exists! Please try different email.')

	username = StringField(label='Username', validators=[InputRequired(message="Username required"), Length(min=4, max=32, message="Username must be between 4 and 32 characters"), DataRequired()])
	email_address=StringField(label='Email', validators=[Email(message="Invalid Email address"), DataRequired()])
	password1 = PasswordField(label='Password', validators=[InputRequired(message="Password required"), Length(min=4, max=32, message="Password must be between 4 and 32 characters"), DataRequired()])
	password2 = PasswordField(label='Confirm Password', validators=[InputRequired(message="Password required"), EqualTo('password1', message="Passwords must match"), DataRequired()])
	submit = SubmitField(label='Submit')


class LoginForm(FlaskForm):
	username = StringField('Username', validators=[InputRequired(message="Username required"), DataRequired()])
	password = PasswordField('Password', validators=[InputRequired(message="Password required"), DataRequired()])
	submit = SubmitField('Log In')

class PurchaseItemForm(FlaskForm):
	submit = SubmitField(label='Purchse Product!')

class SellItemForm(FlaskForm):
	submit = SubmitField(label='Sell Product!')

class SearchForm(FlaskForm):
	searched = StringField('Searched', validators=[DataRequired()])
	submit = SubmitField('Submit')