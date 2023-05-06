from sqlalchemy import Column, String, Float, Integer
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import DeclarativeBase


engine = create_engine('sqlite:///:memory:')


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(120), nullable=False)
    balance = Column(Float, default=0)


Base.metadata.create_all(engine)

