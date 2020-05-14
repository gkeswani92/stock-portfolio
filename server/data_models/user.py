from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from server.database import Base


# To define your models, just subclass the Base class that was
# created by the code in database.py.
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    password = Column(String(120), unique=True)

    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password

    def __repr__(self):
        return f'User(username={self.username})'