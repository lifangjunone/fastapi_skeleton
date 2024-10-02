import os


class DefaultConfig:
    """
    默认配置
    """
    ENV = os.getenv('ENV', 'development')
    PROJECT_NAME = "Fastapi-Skeleton"
    HOST = os.getenv("HOST", "0.0.0.0")
    PORT = int(os.getenv("PORT", 8000))
    DEBUG = False
    VERSION = os.getenv("VERSION", "0.1.0")

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
    debug = True
    RELOAD = True


class TestConfig(DefaultConfig):
    """
    测试环境
    """
    TESTING = True
    RELOAD = True


class ProductionConfig(DefaultConfig):
    """
    生产环境
    """
    DEBUG = False
    RELOAD = False



# 配置映射
configurations = {
    "test": TestConfig,
    "development": DevelopmentConfig,
    "production": ProductionConfig,
}

# 根据环境变量选择配置
config = configurations.get(DefaultConfig.ENV, DefaultConfig).from_env()
