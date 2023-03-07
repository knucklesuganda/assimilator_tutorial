from assimilator.core.database import Repository, UnitOfWork

from dependencies import create_repository, create_uow


def create_user(uow: UnitOfWork):
    with uow:
        uow.repository.save(
            username="Andrey",
            email="python.on.papyrus@gmail.com",
        )

        uow.repository.save(
            username="Andrey-2",
            email="python.on.papyrus-2@gmail.com",
        )

        uow.commit()


def read_user(repository: Repository):
    user = repository.get(
        repository.specs.filter(
            username="Andrey",
        )
    )

    print(user)


def update_user(uow: UnitOfWork):
    with uow:
        user = uow.repository.get(
            uow.repository.specs.filter(
                username="Andrey",
            )
        )

        user.balance += 10
        uow.repository.update(user)
        uow.commit()

        uow.repository.refresh(user)


def delete_user(uow: UnitOfWork):
    with uow:
        user = uow.repository.get(
            uow.repository.specs.filter(
                username="Andrey-2",
            )
        )

        uow.repository.delete(user)
        uow.commit()


if __name__ == '__main__':
    create_user(uow=create_uow())

    read_user(repository=create_repository())
    update_user(create_uow())
    read_user(repository=create_repository())

    delete_user(create_uow())
