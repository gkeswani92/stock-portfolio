from typing import Optional
from typing import List

from server.data_models.stock_exchange import StockExchange
from server.database import db_session


def register_stock_exchange(name: str,) -> StockExchange:
    """Store the stock exchange name in the database"""
    stock_exchange = StockExchange(name=name)
    db_session.add(stock_exchange)
    db_session.commit()
    return stock_exchange


def get_stock_exchange(name: str) -> Optional[StockExchange]:
    """Get stock exchange information"""
    return StockExchange.query.filter(StockExchange.name == name,).one_or_none()


def get_all_stock_exchanges() -> List[StockExchange]:
    """Get all supported stock exchanges"""
    return StockExchange.query.all()
