from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from user import User

import datetime

from base import Base

class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True)
    amount = Column(Integer)
    type = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="transactions")
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

    def __init__(self, amount, type, user_id, username,timestamp):
        self.amount = amount
        self.type = type
        self.user_id = user_id
        self.username = username
        self.timestamp = timestamp

    def __repr__(self):
        return "<Transaction(name='%s', type='%s', amount='%i' on '%s')>" % (self.username, self.type, self.amount, self.lastseen.strftime("%m/%d/%Y, %H:%M:%S"))
