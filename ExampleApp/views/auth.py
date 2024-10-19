
from typing import Union
from ..views import CommonCRUD
from ..models.users import User
from sqlalchemy.orm import Session
from ..schemas.base import CommonResp, CustomFailure
from ExampleApp.exceptions.error_code import ERROR_CODE
from ..schemas.auth import RegistryReq, LoginReq, LoginResp
from ExampleApp.services.auth import sign_jwt, verify_password


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


    @classmethod
    async def login(cls, login: LoginReq, db: Session) -> Union[LoginResp, bool]:
        """
        登录
        """
        user_info = cls.query(db, **{"email": login.email})
        if not user_info:
            return False
        if verify_password(login.password, user_info.password):
            return LoginResp(token=sign_jwt(user_id=user_info.id, email=user_info.email))
        return False