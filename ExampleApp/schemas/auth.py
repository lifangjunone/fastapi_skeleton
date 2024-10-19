from pydantic import model_validator
from ExampleApp.schemas.base import BaseReqSchema, BaseRespSchema
from ExampleApp.services.auth import password_hash
from typing import Optional


class BaseAuthReq(BaseReqSchema):
    """
    Auth Req Base Schema
    """

    email: str
    password: Optional[str] # 密码


    class Config:
        from_attributes = True


class RegistryReq(BaseAuthReq):
    """
    Registry Req Base Schema
    """

    @model_validator(mode='after')
    def convert_plain_hash(self):
        """
        转化明文到hash
        """
        self.password = password_hash(self.password)
        return self


class LoginReq(BaseAuthReq):
    """
    Login Req Base Schema
    """


class BaseAuthResp(BaseRespSchema):
    """
    Auth Resp Base Schema
    """


class LoginResp(BaseAuthResp):
    """
    Login Resp Base Schema
    """
    token: str # token