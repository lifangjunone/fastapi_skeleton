from fastapi import APIRouter
from ..apis.server import ServerApi

router = APIRouter()
router.add_api_route("/version", ServerApi.get_version, summary="获取服务版本")
router.add_api_route("/health-check", ServerApi.health_check, summary="服务健康检查")
