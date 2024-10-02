from typing import List, Dict, AnyStr, Union
from ..schemas.users import UsersResponse


class UserInfo:

    @staticmethod
    async def get_users() -> UsersResponse:
        """
        获取用户列表
        :return:
        """
        users = [
            {"name": "张三", "email": "18612078527@qq.com"},
            {"name": "李四", "email": "18612078528@qq.com"},
        ]
        return UsersResponse(users=users)
