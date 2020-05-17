from flask import abort
from flask import Blueprint
from flask import jsonify
from flask import redirect
from flask import request
from flask import session
from flask import url_for
from string import Template

from server.data_access.user import register_user
from server.data_access.user import UserAlreadyExistsException
from server.exceptions import InvalidLoginCredentialsException
from server.exceptions import MissingCredentialsException
from server.util.auth import validate_login_credentials


PROFILE_PICTURES_PATH = Template(
    './server/images/profile_pictures/$filename.jpg',
)

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

    # Attempt to register the user, save their profile picture and return
    # the appropriate response to the client
    try:
        user = register_user(first_name, last_name, username, password)
        profile_picture.save(
            PROFILE_PICTURES_PATH.substitute(filename=user.id),
        )
    except UserAlreadyExistsException:
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
        response = jsonify({'message': 'INVALID_CREDENTIALS'})
        response.status_code = 400
        return response
    else:
        session.clear()
        session['user_id'] = user.id
        response = jsonify({'message': 'SUCCESS'})
        response.status_code = 200
        return response


@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index_bp.index'))


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
