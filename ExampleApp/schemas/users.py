from .base import BaseSchema
from typing import List


class BaseUser(BaseSchema):
    pass


class UserResp(BaseUser):
    name: str
    email: str


class UsersResp(BaseUser):
    users: List[UserResp]