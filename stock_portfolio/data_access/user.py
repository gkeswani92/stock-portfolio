from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash

from stock_portfolio.data_models.user import User
from stock_portfolio.database import db_session


class UserAlreadyExistsException(Exception):
    pass


def register_user(
    username: str,
    password: str,
):
    """Store user information in the database"""
    user = User(
        username=username,
        password=generate_password_hash(password),
    )
    try:
        db_session.add(user)
        db_session.commit()
    except IntegrityError as e:
        raise UserAlreadyExistsException from e
    else:
        return user

def get_user(
    username: str,
    password: str,
):
    """Get user information from the database"""
    return User(
        username=username,
        password=password,
    )
