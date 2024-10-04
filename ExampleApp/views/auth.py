from ..views import CommonCRUD
from ..models.users import User
from sqlalchemy.orm import Session
from ..schemas.base import CommonResp
from ..schemas.auth import RegistryReq


class AuthViewSet(CommonCRUD):
    model = User

    @classmethod
    async def register(cls, register: RegistryReq, db: Session) -> CommonResp:
        """
        获取用户列表
        :return:
        """
        cls.save(db=db, **register.model_dump())
        return CommonResp()