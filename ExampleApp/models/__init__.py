
from ExampleApp.models.users import User
from common.logger import logger
from databases import Base, engine


def init_table() -> None:
    """
    初始化数据库表
    """
    logger.info(f"开始创建数据库表...")
    Base.metadata.create_all(bind=engine)
    logger.info(f"创建数据库表完成...")




