from ..schemas.users import UsersResp
from sqlalchemy.orm import Session


class UserViewSet:

    @staticmethod
    async def get_users(db: Session) -> UsersResp:
        """
        获取用户列表
        :return:
        """
        users = [
            {"name": "张三", "email": "18612078527@qq.com"},
            {"name": "李四", "email": "18612078528@qq.com"},
        ]
        return UsersResp(users=users)
