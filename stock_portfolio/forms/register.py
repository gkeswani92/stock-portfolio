from flask_wtf import FlaskForm
from wtforms import SubmitField
from wtforms import StringField


class RegisterUserForm(FlaskForm):
    username = StringField('Username')
    password = StringField('Password')
    submit = SubmitField('Register')
