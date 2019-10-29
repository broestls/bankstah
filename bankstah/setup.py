from base import Session, engine, Base
from models import User, Transaction, Brew
from sqlalchemy.orm import relationship

Base.metadata.create_all(engine)

session = Session()

session.commit()
session.close()
