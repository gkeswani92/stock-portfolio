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


def get_user(username: str):
    """Get user information from the database"""
    return User.query.filter(
        User.username == username,
    ).one_or_none()


def get_user_by_id(user_id: int) -> User:
    """Get user information by user_id from the database"""
    return User.query.filter(
        User.id == user_id,
    ).one_or_none()
