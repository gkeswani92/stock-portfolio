import functools

from flask import redirect
from flask import session
from flask import url_for
from werkzeug.security import check_password_hash

from server.data_access.user import get_user
from server.data_models.user import User
from server.exceptions import InvalidLoginCredentialsException


def validate_login_credentials(
    username: str,
    password: str,
):
    # Retrieve the user's information and set the user id in the
    # session if the login credentials are correct
    # check_password_hash() hashes the submitted password in the same
    # way as the stored hash and securely compares them. If they match,
    # the password is valid.
    user: User = get_user(username)
    if not user or not check_password_hash(
        user.password,
        password,
    ):
        raise InvalidLoginCredentialsException('Invalid Login Credentials')
    else:
        return user


def login_required(view):
    """Decorator that will ensure that a view can be only be accessed by
    logged in users
    """
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if not session.get('user_id'):
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view
