from fastapi import FastAPI
from .users import router as user_router
from .server import router as server_router
from .auth import router as auth_router


# 注册路由
def register_routes(app: FastAPI):
    app.include_router(user_router, prefix="/api/v1/users", tags=["users"])
    app.include_router(auth_router, prefix="/api/v1/auth", tags=["auth"])
    app.include_router(server_router, prefix="/server", tags=["server"])