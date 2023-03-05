from assimilator.core.database import BaseModel


class User(BaseModel):
    username: str
    email: str
    balance: float = 0
