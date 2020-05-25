from flask import Blueprint

from server.data_access.follows import get_followees_by_user_id
from server.data_access.transaction import get_transactions_by_user_ids
from server.data_access.user import get_user_info_by_user_ids
from server.constants import OrderType


# Defining a blue print for all URLs that begin with /.
# All views that are related to portfolio should be registered with
# this blueprint and this blueprint will in turn be registred
# with the flask application
feed_bp = Blueprint("feed_bp", __name__, url_prefix="/feed")

PAGINATION_SIZE = 25


@feed_bp.route("/<int:user_id>")
def get_feed_for_user(user_id: int):
    """Return the transactions a user should see on their feed"""
    # Get the list of all users that this user is following and retrieve their
    # user information
    followee_ids = get_followees_by_user_id(user_id)
    user_info = get_user_info_by_user_ids(followee_ids)
    user_id_to_user_info = {user.id: user for user in user_info}

    # Get the transactions for the list of followers and format the response
    transactions = get_transactions_by_user_ids(followee_ids)
    sorted_transactions = sorted(
        transactions, key=lambda x: x.created_at, reverse=True,
    )

    # Pagination:
    # If a list is supposed to have a finite number of entries, we should
    # return all entries. But if at any point, we can have a situation
    # where the number of items returned can be infinite, we should use
    # paging.
    #
    # How can clients request pages?
    # Query strings are commonly used for paging in the following way:
    # /api/sites?page=1&page_size=25
    # You could make an argument for page_size being controlled by the backend
    # but you might also want to give that flexibility to the client
    #
    # Example response with page information:
    # {
    #   totalResults: 255,
    #   nextPage: "api/sites?page=5"
    #   prevPage: "api/sites?page=5"
    #   results: [...]
    # }
    #
    # You can also choose to send the paging details back in the header instead
    # of the body
    return {
        "transactions": [
            {
                "user_id": transaction.user_id,
                "firstName": user_id_to_user_info[
                    transaction.user_id
                ].first_name,
                "lastName": user_id_to_user_info[
                    transaction.user_id
                ].last_name,
                "ticker": transaction.ticker,
                "orderType": OrderType(int(transaction.order_type)).name,
                "price": transaction.price,
                "quantity": transaction.quantity,
                "createdAt": transaction.created_at,
            }
            for transaction in sorted_transactions[:PAGINATION_SIZE]
        ],
        "page": 1,
        "count": len(sorted_transactions[:PAGINATION_SIZE]),
        "total_items": len(sorted_transactions),
    }
