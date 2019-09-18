from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import relationship
import datetime

from base import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    discord_id = Column(String)
    name = Column(String)
    lastseen = Column(DateTime, default=datetime.datetime.utcnow)
    transactions = relationship("Transactions", back_populates="users")

    def __init__(self, discord_id, username, lastseen):
        self.discord_id = discord_id
        self.username = username
        self.lastseen = lastseen

    def __repr__(self):
        return "<User(name='%s', last seen='%s')>" % (self.username, self.lastseen.strftime("%m/%d/%Y, %H:%M:%S"))

    def update_lastseen(self, lastseen):
        self.lastseen = lastseen
