from typing import Union
from pydantic_settings import BaseSettings


class DefaultConfig(BaseSettings):
    """
    默认配置
    """
    ENV: str = 'development'
    PROJECT_NAME: str = "Fastapi-Skeleton"
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    PROTOCOL: str = "http"
    DEBUG: bool = False
    VERSION: str = "0.1.0"
    DATABASE_TYPE: str = "mysql"
    ORM_TYPE: str = "relational"
    RELOAD: bool = True
    class API:
        API_PREFIX: str = "/api/"
        NUMBER = "v1"

    OPENAPI_URL: str = f"{API.API_PREFIX}{API.NUMBER}/openapi.json"
    DOCS_URL: str = f"{API.API_PREFIX}{API.NUMBER}/docs"
    REDOC_URL: str = f"{API.API_PREFIX}{API.NUMBER}/redoc"
    JWT_ALGORITHM: str = 'HS256'
    JWT_SECRET: Union[str, bytes] = b'a0db6b5f227fe7e4b4ca24eee6547f704ab93e5157786c03'

    LOGGING_LEVEL: str = "INFO"


    class Config:
        env_file = "conf/.env"
        env_file_encoding = 'utf-8'
        case_sensitive = True  # 可选: 确保环境变量大小写敏感


    @classmethod
    def from_env(cls):
        """
        从环境变量生成配置实例
        :return:
        """
        return cls()


class DevelopmentConfig(DefaultConfig):
    """
    开发环境
    """

    class Config:
        env_file = "conf/.env"


class TestConfig(DefaultConfig):
    """
    测试环境
    """

    class Config:
        env_file = "conf/.env_test"


class ProductionConfig(DefaultConfig):
    """
    生产环境
    """


    class Config:
        env_file = "conf/.env_prod"


# 配置映射
configurations = {
    "test": TestConfig,
    "development": DevelopmentConfig,
    "production": ProductionConfig,
}

# 根据环境变量选择配置
config = configurations.get(DefaultConfig().ENV, DefaultConfig).from_env()
