from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, EqualTo, ValidationError

from models import User

class RegistrationForm(FlaskForm):
	username = StringField('Username', validators=[InputRequired(message="Username required"), Length(min=4, max=32, message="Username must be between 4 and 32 characters")])
	password = PasswordField('Password', validators=[InputRequired(message="Password required"), Length(min=4, max=32, message="Password must be between 4 and 32 characters")])
	confirm_password = PasswordField('Confirm_password', validators=[InputRequired(message="Password required"), EqualTo('password', message="Passwords must match")
	submit_button = SubmitField('Create')
