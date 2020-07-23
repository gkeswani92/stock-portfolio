from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

from server.database import Base


class Ticker(Base):
    """The ticker table tracks the various stocks listed on the supported
    stock exchanges
    """

    __tablename__ = "ticker"
    __table_args__ = {
        "extend_existing": True,
    }

    id = Column(Integer, primary_key=True)
    exchange_id = Column(
        Integer, ForeignKey("stock_exchange.id", name="fk_stock_exchange_id",),
    )
    ticker = Column(String, nullable=False)
    company_name = Column(String, nullable=False)

    exchange = relationship("StockExchange", backref="ticker")

    def __init__(
        self, exchange_id: int, ticker: str, company_name: str,
    ):
        self.exchange_id = exchange_id
        self.ticker = ticker
        self.company_name = company_name

    def __repr__(self):
        return f"Ticker({self.ticker})"
