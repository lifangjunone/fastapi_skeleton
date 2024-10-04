from pydantic import BaseModel
from typing import TypeVar, Generic

T = TypeVar('T')


class BaseSchema(BaseModel):
    """
    基础schema
    """
    pass


class Response(BaseSchema, Generic[T]):
    """
    HTTP 响应类
    """
    msg: str
    code: int
    data: T


class Success(Response):
    """
    成功响应
    """
    msg: str = 'success'
    code: int = 10000


class Failure(Response):
    """
    失败响应
    """
    msg: str = 'failure'
    code: int = 10001


class CommonResp(BaseSchema):
    is_ok: bool = True
