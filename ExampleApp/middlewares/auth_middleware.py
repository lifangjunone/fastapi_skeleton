from fastapi import Request
from ExampleApp.services.auth import decode_jwt
from ExampleApp.schemas.base import Response
from starlette.middleware.base import BaseHTTPMiddleware
from ExampleApp.exceptions.error_code import ERROR_CODE
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


EXCLUDE_URL_LIST = [
    "login"
]


class TokenValidationMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # 从请求头中获取 token
        token = request.headers.get("Authorization")
        if token and len(token) >= 8:
            token = token[7:]
        if any(exclude_url in request.url.path for exclude_url in EXCLUDE_URL_LIST):
            return await call_next(request)
        if not token:
            return  JSONResponse(
                status_code=401,
                content=jsonable_encoder(Response(code=ERROR_CODE.TOKEN_MISS_ERROR, msg="Token is missing")))
        is_ok, msg = decode_jwt(token)
        if not is_ok:
            return JSONResponse(
                status_code=401,
                content=jsonable_encoder(Response(code=ERROR_CODE.TOKEN_INVALID_ERROR, msg=msg)))
        response = await call_next(request)
        return response