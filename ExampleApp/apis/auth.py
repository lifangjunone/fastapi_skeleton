from fastapi import Depends
from sqlalchemy.orm import Session
from ..dependencies.db import get_db
from ..views.auth import AuthViewSet
from ..schemas.auth import RegistryReq, LoginReq, LoginResp
from ..schemas.base import Success, Response, CommonResp, CustomFailure
from ExampleApp.exceptions.error_code import ERROR_CODE
from typing import Union


class AuthApi:
    """
    用户API
    """

    @staticmethod
    async def login(login: LoginReq, db: Session = Depends(get_db)) -> Response:
        """
        登录， 返回token
        :param login: login info object
        :param db: Session object
        """
        res: Union[LoginResp, bool] = await AuthViewSet.login(login, db)
        if not res:
            return CustomFailure(code=ERROR_CODE.ACCOUNT_OR_PASSWORD_ERROR, msg="账号密码错误")
        return Success(data=res)


    @staticmethod
    async def logout(db: Session = Depends(get_db)) -> Response:
        """
        退出登录， 删除token
        :param db: Session object
        """
        return Success(data={})

    @staticmethod
    async def register(register: RegistryReq, db: Session = Depends(get_db)) -> Response[CustomFailure]:
        """
        注册用户，返回是否成功
        :param db: Session object
        :param register: RegistryReq
        """
        res: CommonResp = await AuthViewSet.register(register, db)
        return Success(data=res)



