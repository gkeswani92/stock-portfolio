from sqlalchemy import Column
from sqlalchemy import Enum
from sqlalchemy import Float
from sqlalchemy import func
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import relationship

from server.database import Base
from server.constants import OrderType


class EquityOrder(Base):
    __tablename__ = "equity_order"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)
    user_id = Column(
        Integer,
        # Defining the foreign key relationship between the `user_id` in this
        # table and the `id` column in the `user` table
        ForeignKey("user.id"),
        nullable=False,
        index=True,
    )
    ticker_id = Column(Integer, ForeignKey("ticker.id"), nullable=False)
    order_type = Column(Enum(OrderType), nullable=False)
    quantity = Column(Float, nullable=False)
    price = Column(Float, nullable=False)
    created_at = Column(
        Integer,
        default=func.unix_timestamp(),
        onupdate=func.unix_timestamp(),
        nullable=False,
    )

    # Defining a relationship between this table and the `Ticker` model so that
    # we can go from every row in this table to the corresponding user.
    # For example: We can do `EquityOrder.ticker.ticker_name` to find the
    # ticker name that corresponds to the ticket_id in a row of this table
    user = relationship("User", backref="order")
    ticker = relationship("Ticker", backref="order")

    def __init__(
        self,
        user_id: int,
        ticker_id: int,
        order_type: OrderType,
        quantity: Float,
        price: float,
    ):
        self.user_id = user_id
        self.ticker_id = ticker_id
        self.order_type = order_type
        self.quantity = quantity
        self.price = price

    def __repr__(self):
        return (
            f"EquityOrder(user_id={self.user_id} "
            f"symbol={self.ticker.ticker} "
            f"order_type={self.order_type} "
            f"quantity={self.quantity} "
            f"price={self.price}) "
        )
