from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from server.database import Base


# To define your models, just subclass the Base class that was
# created by the code in database.py.
# Note: This is the declarative way of using SQLAlchemy where we
# define classes that are mapped to relational database tables
class User(Base):
    __tablename__ = 'user'

    # Including this will mean that we can modify this data model as we go
    # along. Without it, we will get an exception
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(120), nullable=False)

    def __init__(
        self,
        first_name=None,
        last_name=None,
        username=None,
        password=None,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password

    def __repr__(self):
        return f'User(username={self.username})'
