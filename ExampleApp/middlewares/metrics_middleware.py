import time
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from common.logger import logger



class MetricsMiddleware(BaseHTTPMiddleware):
    """
    统计接口相关指标
    1. 客户端ip
    2. 接口耗时
    3. 接口地址
    """
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        client_ip = request.client.host
        url = request.url.path
        response = await call_next(request)
        duration = time.time() - start_time
        logger.info(f"Request from {client_ip} to {url} took {duration:.4f} seconds")
        return response