from assimilator.core.database import UnitOfWork
from assimilator.alchemy.database import AlchemyRepository, AlchemyUnitOfWork
from sqlalchemy.orm import sessionmaker

from models import User, engine

session_creator = sessionmaker(engine)


def get_repository() -> AlchemyRepository:
    session = session_creator()
    return AlchemyRepository(session=session, model=User)


def get_uow() -> UnitOfWork:
    return AlchemyUnitOfWork(repository=get_repository())
