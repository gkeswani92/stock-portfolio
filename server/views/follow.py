from flask import Blueprint
from flask import jsonify

from server.data_access.follows import follow_user
from server.data_access.follows import get_followers_by_user_id
from server.data_access.follows import get_followees_by_user_id
from server.data_access.follows import DuplicateFollowException


# Defining a blue print for all URLs that begin with /portfolio.
# All views that are related to portfolio should be registered with
# this blueprint and this blueprint will in turn be registred
# with the flask application
follow_bp = Blueprint('follow_bp', __name__, url_prefix='/follow')


@follow_bp.route(
    '/<int:follower>/<int:followee>',
    methods=['POST'],
)
def follow(follower: int, followee: int):
    """Follow a user"""
    try:
        follow_user(follower, followee)
    except DuplicateFollowException:
        # We choose to ignore the DuplicateFollowException because we want
        # this API to be idempotent
        pass

    response = jsonify({'message': 'SUCCESS'})
    response.status_code = 200
    return response


@follow_bp.route('/followees/<int:user_id>/', methods=['GET'])
def get_followees_for_user(user_id: int):
    """Get the list of user ids that the user follows"""
    followees = list(get_followees_by_user_id(user_id))
    response = jsonify({
        'message': 'SUCCESS',
        'followees': followees,
    })
    response.status_code = 200
    return response


@follow_bp.route('/followers/<int:user_id>/', methods=['GET'])
def get_followers_for_user(user_id: int):
    """Get the list of user ids that follow a user"""
    followers = list(get_followers_by_user_id(user_id))
    response = jsonify({
        'message': 'SUCCESS',
        'followers': followers,
    })
    response.status_code = 200
    return response
