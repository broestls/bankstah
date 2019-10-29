from sqlalchemy import Column, String, Integer, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import datetime
import time

from base import Base

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    discord_id = Column(String)
    name = Column(String)
    lastseen = Column(DateTime, default=datetime.datetime.utcnow)
    transactions = relationship("Transaction", back_populates="user")

    def __init__(self, discord_id, name, lastseen):
        self.discord_id = discord_id
        self.name =  name
        self.lastseen = lastseen

    def __repr__(self):
        return "<User(name='%s', last seen='%s')>" % (self.username, self.lastseen.strftime("%m/%d/%Y, %H:%M:%S"))

    def update_lastseen(self, lastseen):
        self.lastseen = lastseen

class Transaction(Base):
    __tablename__ = 'transaction'

    id = Column(Integer, primary_key=True)
    amount = Column(Integer)
    type = Column(String)
    user_id = Column(Integer, ForeignKey('user.id'))
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

class Brew(Base):
    __tablename__ = 'brew'

    id = Column(Integer, primary_key=True)
    recipe = Column(String)
    is_tested = Column(Boolean, unique=False, default=False)
    duration = Column(Integer)
    result = Column(String)
    user = Column(String)
    timestamp = Column(DateTime, server_default=func.now())

    def __init__(self, recipe, result, is_tested, duration, user):
        self.recipe = recipe
        self.result = result
        self.is_tested = is_tested
        self.duration = duration
        self.user = user

    def __repr__(self):
        return "<Brew(recipe='%s', result='%s', tested='%s', duration=%i, user=%s at '%s')>" % (self.recipe, self.result, self.is_tested, self.duration, self.user, self.timestamp)
