from typing import Optional
from typing import List

from server.data_models.stock_exchange import StockExchange
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


def get_ticker_symbols_for_exchange(exchange_name: str) -> Optional[List[Ticker]]:
    """Get the list of ticker symbols for the given exchange"""
    if not exchange_name:
        return []

    return (
        db_session.query(Ticker)
        .filter(
            StockExchange.name == exchange_name, StockExchange.id == Ticker.exchange_id,
        )
        .all()
    )

def get_ticker_symbols_fuzzy_match(
    exchange_name: str,
    ticker: str,
) -> Optional[List[Ticker]]:
    """Get the list of ticker symbols for the given exchange that match the `ticker`
    passed in
    """
    if not exchange_name or not ticker:
        return []

    return (
        db_session.query(Ticker)
        .filter(
            StockExchange.name == exchange_name,
            StockExchange.id == Ticker.exchange_id,
            Ticker.ticker.startswith(ticker),
        )
        .all()
    )
