from fastapi import APIRouter
from ..apis.auth import AuthApi

router = APIRouter()

router.add_api_route("/register", AuthApi.register, methods=["POST"], summary="注册用户")