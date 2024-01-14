from sqlalchemy import Column, String, Integer

from .datebase import Base

class User(Base):
    __tablename__ = "UsersApp"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    age = Column(Integer)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)