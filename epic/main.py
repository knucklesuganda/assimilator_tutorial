from assimilator.core.database import Repository, filter_, UnitOfWork

from dependencies import get_repository, get_uow


def create_user(uow: UnitOfWork):
    with uow:
        uow.repository.save(username="Andrey", balance=1000)
        uow.commit()


def read_user(repository: Repository):
    user = repository.get(filter_(username="Andrey"))
    print(user.id, user.username, user.balance)


def add_multiple_users(uow: UnitOfWork):
    with uow:
        uow.repository.save(username="Andrey", balance=1000)
        uow.repository.save(username="Good programmer", balance=1000)
        uow.commit()


if __name__ == '__main__':
    create_user(uow=get_uow())
    read_user(repository=get_repository())
    add_multiple_users(uow=get_uow())
