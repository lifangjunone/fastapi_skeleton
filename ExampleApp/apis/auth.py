from fastapi import Depends
from sqlalchemy.orm import Session
from ..dependencies.db import get_db
from ..views.auth import AuthViewSet
from ..schemas.auth import RegistryReq
from ..schemas.base import Success, Response, CommonResp


class AuthApi:
    """
    用户API
    """

    @staticmethod
    async def login(db: Session = Depends(get_db)) -> Response:
        """
        登录， 返回token
        :param db: Session object
        """
        return Success(data={})


    @staticmethod
    async def logout(db: Session = Depends(get_db)) -> Response:
        """
        退出登录， 删除token
        :param db: Session object
        """
        return Success(data={})

    @staticmethod
    async def register(register: RegistryReq, db: Session = Depends(get_db)) -> Response:
        """
        注册用户，返回是否成功
        :param db: Session object
        :param register: RegistryReq
        """
        res: CommonResp = await AuthViewSet.register(register, db)
        return Success(data=res)



