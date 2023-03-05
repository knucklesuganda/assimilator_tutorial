from assimilator.core.database import Repository, UnitOfWork

from dependencies import create_repository, create_uow
from models import User


def create_user(uow: UnitOfWork):
    with uow:
        new_user = User(
            username="Andrey",
            email="python.on.papyrus@gmail.com",
        )

        new_user2 = User(
            username="Andrey-2",
            email="python.on.papyrus-2@gmail.com",
        )

        uow.repository.save(new_user)
        uow.repository.save(new_user2)
        uow.commit()


def read_user(repository: Repository):
    user = repository.filter(
        repository.specs.filter(
            email="python.on.papyrus@gmail.com",
        )
    )

    print(user)


if __name__ == '__main__':
    try:
        create_user(uow=create_uow())
    except:
        pass
    read_user(
        repository=create_repository(),
    )
