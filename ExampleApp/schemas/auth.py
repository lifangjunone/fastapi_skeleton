from pydantic import model_validator
from ExampleApp.schemas.base import BaseSchema
from ExampleApp.services.auth import password_hash


class BaseAuth(BaseSchema):
    """
    Auth Base Schema
    """
    pass


class RegistryReq(BaseAuth):
    """
    Registry Req Base Schema
    """
    email: str # 邮箱
    password: str # 密码

    class Config:
        from_attributes = True

    @model_validator(mode='after')
    def convert_plain_hash(self, value):
        """
        转化明文到hash
        """
        self.password = password_hash(value)
        return self

