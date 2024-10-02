from fastapi import APIRouter
from ..views.users import UserViewSet

router = APIRouter()

router.add_api_route("/", UserViewSet.get_users, summary="获取用户列表")