from flask import Blueprint
from flask import jsonify
from flask import request

from server.constants import OrderType
from server.data_access.transaction import add_transaction
from server.data_access.transaction import get_transactions_by_user_id


# Defining a blue print for all URLs that begin with /transaction.
# All views that are related to portfolio should be registered with
# this blueprint and this blueprint will in turn be registred
# with the flask application
transaction_bp = Blueprint(
    'transaction_bp',
    __name__,
    url_prefix='/transaction',
)


@transaction_bp.route('/add/<int:user_id>/v1', methods=['POST'])
def add_transaction_by_user(user_id: int):
    """Follow a user"""
    ticker = request.form.get('ticker')
    order_type = OrderType[request.form.get('order_type')]
    price = request.form.get('price')
    quantity = request.form.get('quantity')

    if not all([ticker, price, quantity]):
        response = jsonify({
            'message': 'Please enter the ticker, price, order_type and quantity',
        })
        response.status_code = 400
        return response

    add_transaction(user_id, ticker, order_type, quantity, price)
    response = jsonify({'message': 'SUCCESS'})
    response.status_code = 200
    return response


@transaction_bp.route('/transactions/<int:user_id>/', methods=['GET'])
def get_transactions_for_user(user_id: int):
    """Get the list of user ids that the user follows"""
    transactions = get_transactions_by_user_id(user_id)
    response = jsonify({
        'user_id': user_id,
        'transactions': [
            {
                'ticker': transaction.ticker,
                'order_type': transaction.order_type,
                'price': transaction.price,
                'quantity': transaction.quantity,
                'time': transaction.created_at,
            }
            for transaction in transactions
        ]
    })
    response.status_code = 200
    return response
