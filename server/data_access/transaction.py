from typing import List

from server.data_models.transaction import Transaction
from server.database import db_session
from server.constants import OrderType


def add_transaction(
    user_id: int,
    ticker: str,
    order_type: OrderType,
    quantity: float,
    price: float,
) -> bool:
    """Store the transaction in the database"""
    follows = Transaction(
        user_id=user_id,
        ticker=ticker,
        order_type=order_type,
        quantity=quantity,
        price=price,
    )
    db_session.add(follows)
    db_session.commit()
    return True


def get_transactions_by_user_id(user_id: int) -> List[Transaction]:
    """Get the list of transactions made by the given user"""
    return Transaction.query.filter(
        Transaction.user_id == user_id,
    ).all()


def get_transactions_by_user_ids(user_ids: List[int]) -> List[Transaction]:
    """Get the list of transactions made by the given user ids"""
    return Transaction.query.filter(
        Transaction.user_id.in_(user_ids)
    ).all()
