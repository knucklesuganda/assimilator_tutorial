from sqlalchemy import select
from sqlalchemy.orm import sessionmaker

from bad.database import User, engine


session_creator = sessionmaker(bind=engine)


def create_user():
    user = User(username="Bad programmer", balance=-1000)

    session = session_creator()
    session.add(user)
    session.commit()


def read_user():
    session = session_creator()
    user = session.execute(select(
        User).filter(User.username == "Bad programmer")).first()[0]
    print(user.id, user.username, user.balance)


def add_multiple_users():
    user = User(username="Bad programmer 2", balance=-1000)

    session = session_creator()
    session.add(user)
    session.commit()

    user2 = User(username="Bad programmer 3", balance=-1000)
    session.add(user2)
    session.commit()


if __name__ == '__main__':
    create_user()
    read_user()
    add_multiple_users()
