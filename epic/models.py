from assimilator.mongo.database import MongoModel
from sqlalchemy import Column, String, Float, Integer, Table
from sqlalchemy.orm import registry
from sqlalchemy.engine import create_engine


engine = create_engine('sqlite:///:memory:')
mapper_registry = registry()


users_table = Table(
    'users',
    mapper_registry.metadata,
    Column('id', Integer, primary_key=True),
    Column('username', String(120), nullable=False),
    Column('balance', Float, default=0),
)


class User:
    pass


mapper_registry.map_imperatively(User, users_table)
mapper_registry.metadata.create_all(engine)


class MongoUser(MongoModel):
    class AssimilatorConfig:
        collection = "users"

    username: str
    balance: float = 0
