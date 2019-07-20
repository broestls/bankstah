from base import Sesssion, engine, Base
from transaction import Transaction
from user import User

Base.metadata.create_all(engine)

session = Session()

session.commit()
session.close()
