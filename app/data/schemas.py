from pydantic import BaseModel
from datetime import datetime

# example
class ResponseUser(BaseModel):
    id: int
    userName: str
    password: str
    firstName: str
    lastName: str
    telephone: int
    createdAt: datetime
    modifiedAt: datetime
    
class RequestUser(BaseModel):
    userName: str
    password: str
    firstName: str
    lastName: str
    telephone: int