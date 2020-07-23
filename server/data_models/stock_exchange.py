from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from server.database import Base


class StockExchange(Base):
    """The exchange table tracks the various stock exchanges supported by our
    web application
    """

    __tablename__ = "stock_exchange"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True, index=True)

    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return f"StockExchange({self.name})"
