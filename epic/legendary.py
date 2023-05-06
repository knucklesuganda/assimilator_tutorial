from dependencies import get_service


if __name__ == '__main__':
    crud = get_service(source="alchemy")

    crud.create({
        "username": "Andrey",
        "balance": 1000,
    })

    user = crud.get(username="Andrey")
    print(user.id, user.username, user.balance)
