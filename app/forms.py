from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import InputRequired, Length, EqualTo, ValidationError
from app.models import User

class RegistrationForm(FlaskForm):
    username = StringField(label='Username', validators=[InputRequired(message="Username required"), Length(min=4, max=32, message="Username must be between 4 and 32 characters")])
    email_address=StringField(label='Email')
    password = PasswordField(label='Password', validators=[InputRequired(message="Password required"), Length(min=4, max=32, message="Password must be between 4 and 32 characters")])
    confirm_password = PasswordField(label='Confirm password', validators=(InputRequired(message="Password required"), EqualTo('password', message="Passwords must match")))
    submit = SubmitField(label='Submit')

    def validate_username(self, username):
        user_object = User.query.filter_by(username=username.data).first()
        if user_object:
            raise ValidationError("Username already exist")

'''def credentials(form, field):
    username_entry = form.username.data
    password_entry = field.data
    user_object = User.query.filter_by(username=username.data).first()
    if user_object in None:
        raise ValidationError("Username or password is incorrect")
    elif password_entry != user_object.password:
        raise ValidationError("Username or password is incorrect")

class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(message="Username required")])
    password = StringField('password', validators=[InputRequired(message="Password required"), credentials])
    submit = SubmitField('Login')'''
