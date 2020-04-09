from werkzeug.security import check_password_hash

from stock_portfolio.data_access.user import get_user


class InvalidLoginCredentialsException(Exception):
    pass


def validate_login_credentials(
    username: str,
    password: str,
):
    # Retrieve the user's information and set the user id in the
    # session if the login credentials are correct
    user = get_user(username, password)
    if not user.username == username or not check_password_hash(
        user.password,
        password,
    ):
        raise InvalidLoginCredentialsException
