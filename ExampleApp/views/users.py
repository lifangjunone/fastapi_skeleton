from typing import List, Dict, AnyStr, Union


class UserViewSet:

    @staticmethod
    async def get_users() -> List[Dict[str, Union[AnyStr, int]]]:
        """
        获取用户列表
        :return:
        """
        users = [
            {"name": "张三", "email": "18612078527@qq.com"},
            {"name": "李四", "email": "18612078528@qq.com"},
        ]
        return users
