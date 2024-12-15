from beanie import Document
from datetime import datetime


# exmaple
class User(Document):
    id: int
    userName: str
    password: str
    firstName: str
    lastName: str
    telephone: int
    createdAt: datetime
    modifiedAt: datetime
