from flask import abort
from flask import Blueprint
from flask import flash
from flask import jsonify
from flask import render_template
from flask import redirect
from flask import request
from flask import session
from flask import url_for

from stock_portfolio.data_access.user import register_user
from stock_portfolio.data_access.user import UserAlreadyExistsException
from stock_portfolio.exceptions import InvalidLoginCredentialsException
from stock_portfolio.exceptions import MissingCredentialsException
from stock_portfolio.util.auth import validate_login_credentials

# Defining a blue print for all URLs that begin with /auth.
# All views that are related to auth should be registered with
# this blueprint and this blueprint will in turn be registred
# with the flask application
auth_bp = Blueprint('auth', __name__, url_prefix='/auth')


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    # Case: When the register view is called with HTTP GET, we return
    # a form where the user can enter their username and password
    if request.method == 'GET':
        return render_template('auth/register.html')

    # Case: When the register view is called with HTTP POST, we try to
    # register them in the database
    else:
        # request.form is a special type of dict mapping submitted form keys
        # and values.
        username = request.form.get('username')
        password = request.form.get('password')
        if not username or not password:
            abort(400)

        # Attempt to register the user and return the appropriate response
        # to the client
        try:
            register_user(username, password)
        except UserAlreadyExistsException:
            return render_template('auth/register.html')
        else:
            return redirect(url_for('portfolio_bp.index'))


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('auth/login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')

        # Raise a MissingCredentialsException if the username or password are
        # missing. This maps to a 400 Bad Request and results in a JSON response
        # because of the error handler defined below
        if not username or not password:
            raise MissingCredentialsException('Username and password are required fields')

        # Retrieve the user's information and set the user id in the
        # session if the login credentials are correct
        try:
            user = validate_login_credentials(username, password)
        except InvalidLoginCredentialsException:
            flash('Invalid Login Credentials')
            return render_template('auth/login.html')
        else:
            # session is a dict that stores data across requests. When validation
            # succeeds, the user’s id is stored in a new session. The data is stored
            # in a cookie that is sent to the browser, and the browser then sends it
            # back with subsequent requests. Flask securely signs the data so that it
            # can’t be tampered with.
            session.clear()
            session['user_id'] = user.id

            # The url_for() function generates the URL to a view based on a name
            # and arguments. The name associated with a view is also called the
            # endpoint, and by default it’s the same as the name of the view function.
            return redirect(url_for('portfolio_bp.index'))


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
