import uvicorn
from conf.default import config
from fastapi import FastAPI, Depends
from ExampleApp.models import init_table
from contextlib import asynccontextmanager
from common.logger import setup_logger, logger
from ExampleApp.routers import register_routes


async def print_server_info():
    """
    打印服务信息
    """
    logger.info(f"Server version: {config.VERSION}")
    logger.info(f"Server API prefix: {config.API.API_PREFIX}")
    logger.info(f"Server API prefix version: {config.API.NUMBER}")
    logger.info(f"Server logging level: {config.LOGGING_LEVEL}")
    logger.info(f"Server address: {config.PROTOCOL}://{config.HOST}:{config.PORT}")
    logger.info(f"Server Docs address: {config.PROTOCOL}://{config.HOST}:{config.PORT}/{config.DOCS_URL}")
    logger.info(f"Server Redoc address: {config.PROTOCOL}://{config.HOST}:{config.PORT}/{config.REDOC_URL}")



@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    生命周期函数
    :param app: 应用实例
    :return:
    """
    # 应用启动时执行的代码
    # 设置logger
    setup_logger()
    # 注册路由
    register_routes(app)
    # 初始化数据库表
    if config.DEBUG:
        logger.info(f"Run server is a debug mode")
        await print_server_info()
        init_table()
    logger.info(f"Starting {config.PROJECT_NAME}:{config.VERSION} app...")
    yield
    # 应用关闭时执行的代码
    logger.info(f"Shutting down {config.PROJECT_NAME}:{config.VERSION} app...")


def create_app() -> FastAPI:
    """
    创建 FastAPI 应用实例，并注册生命周期事件
    :return: FastAPI 实例
    """
    app: FastAPI = FastAPI(
        lifespan=lifespan,
        title=config.PROJECT_NAME,
        version=config.VERSION,
        reload=config.RELOAD,
        docs_url=config.DOCS_URL,
        redoc_url=config.REDOC_URL,
        openapi_url=config.OPENAPI_URL,
    )
    return app



def run_app():
    """
    启动 FastAPI 服务
    :return: None
    """

    app: FastAPI = create_app()
    uvicorn.run(app, host=config.HOST, port=config.PORT)


if __name__ == '__main__':
    run_app()
