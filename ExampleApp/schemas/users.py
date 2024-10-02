from pydantic import BaseModel
from typing import List


class BaseUser(BaseModel):
    pass


class UserResponse(BaseUser):
    name: str
    email: str


class UsersResponse(BaseUser):
    users: List[UserResponse]