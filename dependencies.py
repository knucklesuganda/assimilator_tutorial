from assimilator.core.database import Repository
from assimilator.internal.database import InternalRepository

from models import User

database = {}


def get_repository() -> Repository:
    return InternalRepository(
        session=database,
        model=User,
    )

