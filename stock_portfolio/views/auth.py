from flask import Blueprint
from flask import request
from werkzeug.exceptions import BadRequest
from werkzeug.exceptions import InternalServerError

from stock_portfolio.data_access.user import register_user

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
        pass

    # Case: When the register view is called with HTTP POST, we try to
    # register them in the database
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        if not username or not password:
            raise BadRequest('Username and password are required fields')

        # Attempt to register the user
        user = register_user(username, password)
        if not user:
            raise InternalServerError(f'Could not register {username}')

        return {
            'status_code': 200,
            'username': username,
        }
