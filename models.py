from database import Base
from sqlalchemy import String, Integer, Column


class User(Base):
    __tablename__= "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    family = Column(String)
    password = Column(String)
    email = Column(String, unique=True)