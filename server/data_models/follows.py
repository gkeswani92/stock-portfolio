from sqlalchemy import Column
from sqlalchemy import Integer
from server.database import Base


class Follows(Base):
    """The follower table is used to keep track of users that follow
    other users
    """
    __tablename__ = 'follows'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    follower = Column(Integer, nullable=False)
    followee = Column(Integer, nullable=False)

    def __init__(self, followee=None, follower=None):
        self.follower = follower
        self.followee = followee

    def __repr__(self):
        return f'Follows({self.follower}->{self.followee})'
