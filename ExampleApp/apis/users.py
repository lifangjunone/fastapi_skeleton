from ..views.users import UserInfo
from ..schemas.base import Success, Response
from ..schemas.users import UsersResponse


class UsersApi:
    """
    用户API
    """

    @staticmethod
    async def get_users() -> Response[UsersResponse]:
        """
        获取用户信息
        """
        users: UsersResponse = await UserInfo.get_users()
        return Success(data=users)
