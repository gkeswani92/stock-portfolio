from werkzeug.security import check_password_hash

from stock_portfolio.data_access.user import get_user
from stock_portfolio.data_models.user import User
from stock_portfolio.exceptions import InvalidLoginCredentialsException


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