from sqlalchemy import Column, String, Integer, DateTime
import datetime
from base import Base

class Bank(Base):
    __tablename__ = 'bank'

    id = Column(Integer, primary_key=True)
    total = Column(Integer)
    transactions = Column(Integer)

    def __init__(self, total, transactions):
        self.total = total
        self.transactions = total
