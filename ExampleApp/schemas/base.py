from datetime import datetime
from pydantic import BaseModel, model_validator
from typing import TypeVar, Generic, Any, Union, Optional
from ExampleApp.exceptions.error_code import ErrorCode
from utils.time_utils import format_datetime

T = TypeVar('T')


class BaseSchema(BaseModel):
    """
    基础schema
    """

    class Config:
        # 排除未设置的字段
        exclude_unset = True



class BaseReqSchema(BaseSchema):
    """
    基础Req Schema
    """
    pass


class BaseRespSchema(BaseSchema):
    """
    基础Resp Schema
    """

    @model_validator(mode='after')
    def format_create_date(self):
        """
        转化 create_date 为格式化字符串
        """
        if hasattr(self, 'create_date') and isinstance(self.create_date, datetime):
            self.create_date = format_datetime(self.create_date)
        return self



class Response(BaseRespSchema, Generic[T]):
    """
    HTTP 响应类
    """
    msg: str
    code: Union[int, ErrorCode]
    data: T = {}


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


class CustomFailure(Response):
    """
    自定义错误信息
    """

    def __init__(self, code: Union[int, str], msg: str = '', data: Any = None):
        if data is None:
            data = {}
        super().__init__(msg=msg, code=code, data=data)



class CommonResp(BaseRespSchema):
    is_ok: bool = True
