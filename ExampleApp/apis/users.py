from fastapi import Depends
from sqlalchemy.orm import Session
from ..views.users import UserViewSet
from ..dependencies.db import get_db
from ..schemas.users import UsersResp
from ..schemas.base import Success, Response


class UsersApi:
    """
    用户API
    """

    @staticmethod
    async def get_users(db: Session = Depends(get_db)) -> Response[UsersResp]:
        """
        获取用户信息
        :param db: Session object
        """
        users: UsersResp = await UserViewSet.get_users(db)
        return Success(data=users)
