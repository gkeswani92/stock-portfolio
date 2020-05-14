from flask_wtf import FlaskForm
from wtforms import SubmitField
from wtforms import StringField
from wtforms.validators import DataRequired
from wtforms.validators import InputRequired
from wtforms.validators import Length


class RegisterUserForm(FlaskForm):
    username = StringField(
        'Username',
        validators=[
            InputRequired('Username is required!'),
            DataRequired('Username is required!'),
            Length(
                min=5,
                max=20,
                message='Username must be between 5 and 20 characters',
            ),
        ]
    )
    password = StringField(
        'Password',
        validators=[
            InputRequired('Username is required!'),
            DataRequired('Username is required!'),
        ]
    )
    submit = SubmitField('Register')
