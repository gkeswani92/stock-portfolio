import datetime

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship
from server.database import Base


class Transaction(Base):
    __tablename__ = 'transaction'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    user_id = Column(
        Integer,
        # Defining the foreign key relationship between the `user_id` in this
        # table and the `id` column in the `user` table
        ForeignKey('user.id'),
        nullable=False,
    )
    ticker = Column(String(16), nullable=False)
    quantity = Column(Float, nullable=False)
    price = Column(Float, nullable=False)
    created_at = Column(
        DateTime,
        default=datetime.datetime.utcnow,
        nullable=False,
    )

    # Defining a relationship between this table and the `User` model so that
    # we can go from every row in this table to the corresponding user.
    User = relationship('User', backref='transaction')

    def __init__(self, user_id, ticker, quantity, price):
        self.user_id = user_id
        self.ticker = ticker
        self.quantity = quantity
        self.price = price

    def __repr__(self):
        return f'Transaction(user_id={self.user_id} ' \
               f'symbol={self.ticker} quantity={self.quantity} ' \
               f'price={self.price}'
