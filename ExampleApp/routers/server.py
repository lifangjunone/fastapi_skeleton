from fastapi import APIRouter
from ..views.server import ServerInfo

router = APIRouter()
router.add_api_route("/version", ServerInfo.get_version, summary="获取服务版本")
router.add_api_route("/health-check", ServerInfo.health_check, summary="服务健康检查")
