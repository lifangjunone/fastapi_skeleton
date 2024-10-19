from fastapi import APIRouter
from ..apis.auth import AuthApi

router = APIRouter()

router.add_api_route("/register", AuthApi.register, methods=["POST"], summary="注册用户")
router.add_api_route("/login", AuthApi.login, methods=["POST"], summary="登录")