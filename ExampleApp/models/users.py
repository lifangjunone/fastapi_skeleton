
from ..models.base import BaseModel
from sqlalchemy import Column, String, Boolean


class User(BaseModel):
    __tablename__ = 'users'

    email = Column(String(32), unique=True, index=True, comment="Email address")
    password = Column(String(256), comment="密码")
    is_active = Column(Boolean, default=True, nullable=True, comment="是否已激活")


