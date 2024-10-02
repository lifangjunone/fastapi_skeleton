from ..views.server import ServerInfo
from ..schemas.base import Success, Response
from ..schemas.server import HealthCheckResponse, VersionInfoResponse


class ServerApi:

    @staticmethod
    async def get_version() -> Response[VersionInfoResponse]:
        """
        获取服务版本
        """
        svr: VersionInfoResponse = await ServerInfo.get_version()
        return Success(data=svr)

    @staticmethod
    async def health_check() -> Response[HealthCheckResponse]:
        hck: HealthCheckResponse = await ServerInfo.health_check()
        return Success(data=hck)