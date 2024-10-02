from fastapi import APIRouter
from ..apis.users import UsersApi

router = APIRouter()

router.add_api_route("/", UsersApi.get_users, summary="获取用户列表")