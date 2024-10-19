from .base import BaseRespSchema
from typing import List, Union
from datetime import datetime


class BaseRespUser(BaseRespSchema):
    """
    基础 Base User Resp
    """
    pass


class UserResp(BaseRespUser):
    """
    单个用户
    """
    id: int
    email: str
    create_date: Union[datetime, str]
    created_by: Union[str, None] = ''


class UsersResp(BaseRespUser):
    """
    用户列表
    """
    users: List[UserResp]