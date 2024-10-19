from typing import List
from ..views import CommonCRUD
from sqlalchemy.orm import Session
from ..schemas.users import UsersResp
from ExampleApp.models.users import User
from fastapi.encoders import jsonable_encoder


class UserViewSet(CommonCRUD):
    model = User
    default_exclude_fields = ["is_deleted", "password"]

    @classmethod
    async def get_users(cls, db: Session) -> UsersResp:
        """
        获取用户列表
        :return:
        """
        users: List = cls.query(db, many=True)
        return UsersResp(users=jsonable_encoder(users))
