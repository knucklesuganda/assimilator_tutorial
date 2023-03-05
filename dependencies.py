from assimilator.core.database import Repository, UnitOfWork
from assimilator.internal.database import InternalRepository,\
    InternalUnitOfWork

from models import User


database = {}


def create_repository() -> Repository:
    return InternalRepository(
        session=database,
        model=User,
    )


def create_uow() -> UnitOfWork:
    return InternalUnitOfWork(
        repository=create_repository(),
    )
