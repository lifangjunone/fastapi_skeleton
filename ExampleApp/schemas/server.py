from pydantic import BaseModel

class ServerBase(BaseModel):
    """
    服务基础类
    """
    pass


class HealthCheckResponse(ServerBase):
    """
    检查检查响应schema
    """
    msg: str
    success: bool