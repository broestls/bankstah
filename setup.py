from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import datetime
import config

engine = create_engine(config.DATABASE_URL, echo=True)

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    lastseen = Column(DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return "<User(name='%s', last seen='%s')>" % (self.username, self.lastseen.strftime("%m/%d/%Y, %H:%M:%S"))

class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True)
    amount = Column(Integer)
    type = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="transactions")
    lastseen = Column(DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return "<Transaction(name='%s', type='%s', amount='%i' on '%s')>" % (self.username, self.type, self.amount, self.lastseen.strftime("%m/%d/%Y, %H:%M:%S"))

class Bank(Base):
    __tablename__ = 'bank'

    id = Column(Integer, primary_key=True)
    total = Column(Integer)
    transactions = Column(Integer)

Base.metadata.create_all(engine)
