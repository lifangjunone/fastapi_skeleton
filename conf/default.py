import os
from pydantic_settings import BaseSettings


class DefaultConfig(BaseSettings):
    """
    默认配置
    """
    ENV: str = 'development'
    PROJECT_NAME: str = "Fastapi-Skeleton"
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    DEBUG: bool = False
    VERSION: str = "0.1.0"


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
    debug: bool = True
    RELOAD: bool = True


class TestConfig(DefaultConfig):
    """
    测试环境
    """
    TESTING: bool = True
    RELOAD: bool = True


class ProductionConfig(DefaultConfig):
    """
    生产环境
    """
    DEBUG: bool = False
    RELOAD: bool = False


# 配置映射
configurations = {
    "test": TestConfig,
    "development": DevelopmentConfig,
    "production": ProductionConfig,
}

# 根据环境变量选择配置
config = configurations.get(DefaultConfig().ENV, DefaultConfig).from_env()
