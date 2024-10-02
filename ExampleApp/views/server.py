from conf.default import config
from typing import Dict, AnyStr, Union
from fastapi.encoders import jsonable_encoder
from ..schemas.server import HealthCheckResponse

class ServerInfo:
    """
    服务信息
    """

    @staticmethod
    async def get_version() -> Dict[str, AnyStr]:
        """
        获取服务版本
        :return:
        """
        version = {
            "version": config.VERSION
        }
        return version


    @staticmethod
    async def health_check() -> HealthCheckResponse:
        """
        健康检查
        :return:
        """
        return HealthCheckResponse(msg="ok", success=True)