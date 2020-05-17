from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from server.database import Base


# To define your models, just subclass the Base class that was
# created by the code in database.py.
class User(Base):
    __tablename__ = 'user'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    username = Column(String(50), unique=True)
    password = Column(String(120))

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
