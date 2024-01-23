from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = "User"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    age = Column(Integer)
    email = Column(String, nullable=False, unique=True)
    hashed_password = Column(String, nullable=False)

    token = relationship("Token", back_populates="user")

class Token(Base):
    __tablename__ = "Token"

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    access_token = Column(String, unique=True, index=True)

    user_id = Column(Integer, ForeignKey('User.id'))
    user = relationship("User", back_populates="token")