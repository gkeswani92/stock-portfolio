from typing import List
from typing import Optional

from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash

from server.data_models.user import User
from server.database import db_session


class UserAlreadyExistsException(Exception):
    pass


def register_user(
    first_name: str,
    last_name: str,
    username: str,
    password: str,
) -> User:
    """Store user information in the database"""
    user = User(
        first_name=first_name,
        last_name=last_name,
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


def get_user(username: str) -> Optional[User]:
    """Get user information from the database"""
    return User.query.filter(
        User.username == username,
    ).one_or_none()


def get_user_by_id(user_id: int) -> Optional[User]:
    """Get user information by user_id from the database"""
    return User.query.filter(
        User.id == user_id,
    ).one_or_none()


def get_user_info_by_user_ids(user_ids: List[int]) -> List[User]:
    return User.query.filter(
        User.id.in_(user_ids),
    ).all()
