from sqlalchemy.exc import IntegrityError

from server.data_models.follows import Follows
from server.database import db_session


class DuplicateFollowException(Exception):
    pass


def follow_user(
    follower: int,
    followee: int,
):
    """Store the follows relationship in the database"""
    follows = Follows(
        follower=follower,
        followee=followee,
    )
    try:
        db_session.add(follows)
        db_session.commit()
    except IntegrityError as e:
        raise DuplicateFollowException from e

    return True


def get_followees_by_user_id(user_id: int):
    """Get the list of user_ids that are followed by the given user id"""
    result = Follows.query.filter(
        Follows.follower == user_id,
    ).all()

    return {row.followee for row in result}


def get_followers_by_user_id(user_id: int):
    """Get the list of user_ids that are following the given user id"""
    result = Follows.query.filter(
        Follows.followee == user_id,
    ).all()

    return {row.follower for row in result}
