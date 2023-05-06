from pymongo import MongoClient
from assimilator.core.database import UnitOfWork
from assimilator.alchemy.database import AlchemyRepository, AlchemyUnitOfWork
from assimilator.core.services import CRUDService
from assimilator.mongo.database import MongoUnitOfWork, MongoRepository
from sqlalchemy.orm import sessionmaker

from models import User, engine, MongoUser

session_creator = sessionmaker(engine)


def get_repository() -> AlchemyRepository:
    session = session_creator()
    return AlchemyRepository(session=session, model=User)


def get_uow() -> UnitOfWork:
    return AlchemyUnitOfWork(repository=get_repository())


def get_service(source: str = "alchemy") -> CRUDService:
    if source == "alchemy":
        return CRUDService(uow=get_uow())
    else:
        session = MongoClient()
        repository = MongoRepository(session=session, model=MongoUser, database="test_users")
        uow = MongoUnitOfWork(repository=repository)
        return CRUDService(uow=uow)
