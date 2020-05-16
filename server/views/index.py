from flask import Blueprint
from flask import render_template

from server.data_access.follows import get_followees_by_user_id
from server.data_access.transaction import get_transactions_by_user_ids


# Defining a blue print for all URLs that begin with /.
# All views that are related to portfolio should be registered with
# this blueprint and this blueprint will in turn be registred
# with the flask application
index_bp = Blueprint('index_bp', __name__, url_prefix='/')

PAGINATION_SIZE = 10


@index_bp.route('/')
def index():
    # Render a jinja template by passing in variables and returning HTML
    # to the caller of this API
    # The path we are passing into render template is just considered to be
    # a text file with placeholders. After the placeholders are filled in,
    # we will render the HTML and then return it to the caller
    return render_template(
        'index.html',
        message='Test message from the backend',
    )


@index_bp.route('/feed/<int:user_id>')
def get_feed_for_user(user_id: int):
    """Return the transactions a user should see on their feed"""
    # Get the list of all users that this user is following and retrieve their
    # user information
    followee_ids = get_followees_by_user_id(user_id)

    # Get the transactions for the list of followers and format the response
    transactions = get_transactions_by_user_ids(followee_ids)
    sorted_transactions = sorted(
        transactions,
        key=lambda x: x.created_at,
        reverse=True,
    )
    return {
        'transactions': [
            {
                'user_id': transaction.user_id,
                'ticker': transaction.ticker,
                'price': transaction.price,
                'quantity': transaction.quantity,
                'created_at': transaction.created_at,
            }
            for transaction in sorted_transactions[:PAGINATION_SIZE]
        ],
        'page': 1,
        'count': len(sorted_transactions[:PAGINATION_SIZE]),
        'total_items': len(sorted_transactions),
    }
