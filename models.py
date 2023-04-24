from assimilator.core.database import BaseModel


class User(BaseModel):
    username: str
    balance: float = 0
