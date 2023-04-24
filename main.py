from assimilator.core.database import Repository, filter_

from dependencies import get_repository


def create_user(repository: Repository):
    user = repository.save(
        username="Andrey",
        balance=1000000,
    )
    return user.id


def read_user(id: str, repository: Repository):
    user = repository.get(filter_(id=id))
    print(user)


if __name__ == '__main__':
    user_id = create_user(repository=get_repository())
    read_user(id=user_id, repository=get_repository())
