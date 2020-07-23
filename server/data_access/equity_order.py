from typing import List

from server.data_access.ticker import get_ticker_symbol
from server.data_models.equity_order import EquityOrder
from server.database import db_session
from server.constants import OrderType


def add_equity_order(
    user_id: int, ticker: str, order_type: OrderType, quantity: float, price: float,
) -> bool:
    """Store the equity order in the database"""
    ticker_info = get_ticker_symbol(ticker)
    if not ticker_info:
        raise ValueError("Invalid ticker symbol")

    user_transaction = EquityOrder(
        user_id=user_id,
        ticker_id=ticker_info.id,
        order_type=order_type,
        quantity=quantity,
        price=price,
    )
    db_session.add(user_transaction)
    db_session.commit()
    return user_transaction


def get_equity_orders_by_user_id(user_id: int) -> List[EquityOrder]:
    """Get the list of transactions made by the given user"""
    return EquityOrder.query.filter(EquityOrder.user_id == user_id,).all()


def get_equity_orders_by_user_ids(user_ids: List[int]) -> List[EquityOrder]:
    """Get the list of transactions made by the given user ids"""
    return EquityOrder.query.filter(EquityOrder.user_id.in_(user_ids)).all()
