from flask import Blueprint
from flask import jsonify
from flask import request
from flask import session
from string import Template

from server.data_access.user import get_user_by_id
from server.data_access.user import register_user
from server.data_access.user import UserAlreadyExistsException
from server.exceptions import InvalidLoginCredentialsException
from server.exceptions import MissingCredentialsException
from server.util.auth import validate_login_credentials


PROFILE_PICTURES_PATH = Template(
    './server/images/profile_pictures/$filename.jpg',
)
ALLOWED_CONTENT_TYPES = {'image/jpeg'}

# Defining a blue print for all URLs that begin with /auth.
# All views that are related to auth should be registered with
# this blueprint and this blueprint will in turn be registred
# with the flask application
auth_bp = Blueprint('auth', __name__, url_prefix='/auth')


# By default, all view controllers support the GET method
@auth_bp.route('/register', methods=['POST'])
def register():
    # Case: When the register view is called with HTTP POST, we try to
    # register them in the database
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    username = request.form.get('username')
    password = request.form.get('password')
    profile_picture = request.files.get('profile_picture')

    if not all([first_name, last_name, username, password, profile_picture]):
        response = jsonify({'message': 'MISSING_DATA'})
        response.status_code = 400
        return response

    if profile_picture.content_type not in ALLOWED_CONTENT_TYPES:
        print('bad image')
        response = jsonify({'message': 'UNSUPPORTED_CONTENT_TYPE'})
        response.status_code = 400
        return response

    # Attempt to register the user, save their profile picture and return
    # the appropriate response to the client
    try:
        user = register_user(first_name, last_name, username, password)
        profile_picture.save(
            PROFILE_PICTURES_PATH.substitute(filename=user.id),
        )
    except UserAlreadyExistsException:
        print('user exists')
        response = jsonify({'message': 'USER_ALREADY_EXISTS'})
        response.status_code = 400
        return response
    else:
        session['user_id'] = user.id
        response = jsonify({'message': 'SUCCESS'})
        response.status_code = 200
        return response


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    # Raise a MissingCredentialsException if the username or password are
    # missing. This maps to a 400 Bad Request and results in a JSON response
    # because of the error handler defined below
    if not username or not password:
        response = jsonify({
            'message': 'Please enter the username and password',
        })
        response.status_code = 400
        return response

    # Retrieve the user's information and set the user id in the
    # session if the login credentials are correct
    try:
        user = validate_login_credentials(username, password)
    except InvalidLoginCredentialsException:
        # Error handling
        # We want to return a 400 Bad Request to tell the user that there was
        # something wrong with their request but we also want to supply an
        # error message to tell them what was wrong so that they can correct
        # their mistake in the follow up call

        # Note: It is important to be careful with drawing the line between
        # a very generic message and a very specific message.
        # For example: It is not a good idea to return messages like 'Wrong
        # Password' or 'Username does not exist' since it gives the hacker
        # an idea of how they can break the system. Instead provide a more
        # generic error like 'Invalid Credentials' so that they know
        # something was wrong with the credentials but not exactly what was
        # wrong
        response = jsonify({'message': 'INVALID_CREDENTIALS'})
        response.status_code = 400
        return response
    else:
        session.clear()
        session['user_id'] = user.id
        response = jsonify({'message': 'SUCCESS'})
        response.status_code = 200
        return response


@auth_bp.route('/is_logged_in')
def is_logged_in():
    is_logged_in = 'user_id' in session
    if not is_logged_in:
        return {'is_logged_in': False}

    user = get_user_by_id(user_id=session['user_id'])
    return {
        'is_logged_in': True,
        'user': {
            'user_id': user.id,
            'username': user.username,
        }
    }


@auth_bp.route('/logout', methods=['POST'])
def logout():
    session.clear()
    response = jsonify({'logged_out': True})
    response.status_code = 200
    return response


@auth_bp.errorhandler(InvalidLoginCredentialsException)
def handle_invalid_login_credentials(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@auth_bp.errorhandler(MissingCredentialsException)
def handle_missing_credentials(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response
