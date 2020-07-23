from typing import Optional

from server.data_models.ticker import Ticker
from server.database import db_session


def register_ticker_symbol(exchange_id: int, ticker: str, company_name: str,) -> Ticker:
    """Store the ticker information in the database"""
    ticker = Ticker(exchange_id=exchange_id, ticker=ticker, company_name=company_name)
    db_session.add(ticker)
    db_session.commit()
    return ticker


def get_ticker_symbol(ticker: str) -> Optional[Ticker]:
    """Get stock exchange information"""
    return Ticker.query.filter(Ticker.ticker == ticker,).one_or_none()
