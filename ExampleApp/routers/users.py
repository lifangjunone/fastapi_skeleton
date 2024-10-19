from fastapi import APIRouter
from ..apis.users import UsersApi

router = APIRouter()

router.add_api_route("/list", UsersApi.get_users, methods=["GET"], summary="获取用户列表")