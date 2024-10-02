from conf.default import config
from ..schemas.server import HealthCheckResponse, VersionInfoResponse

class ServerInfo:
    """
    服务信息
    """

    @staticmethod
    async def get_version() -> VersionInfoResponse:
        """
        获取服务版本
        :return:
        """
        return VersionInfoResponse(version=config.VERSION)


    @staticmethod
    async def health_check() -> HealthCheckResponse:
        """
        健康检查
        :return:
        """
        return HealthCheckResponse(msg="ok", success=True)