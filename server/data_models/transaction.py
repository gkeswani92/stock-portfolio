import datetime

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Float
from sqlalchemy import Integer
from sqlalchemy import String
from server.database import Base


class Transaction(Base):
    __tablename__ = 'transaction'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    ticker = Column(String(16))
    quantity = Column(Float)
    price = Column(Float)
    created_at = Column(
        DateTime,
        default=datetime.datetime.utcnow,
    )

    def __init__(self, user_id, ticker, quantity, price):
        self.user_id = user_id
        self.ticker = ticker
        self.quantity = quantity
        self.price = price

    def __repr__(self):
        return f'Transaction(user_id={self.user_id} ' \
               f'symbol={self.ticker} quantity={self.quantity} ' \
               f'price={self.price}'
