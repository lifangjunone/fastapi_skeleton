from pathlib import Path
from conf.default import config
from typing import Dict, AnyStr
from common.logger import logger
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from databases.mysql_impl import SQLALCHEMY_DATABASE_URL as mysql_url
from databases.postgres_impl import SQLALCHEMY_DATABASE_URL as postgres_url


def get_all_db_impl() -> Dict[str, AnyStr]:
    """
    获取所有数据库实现
    """
    db_impl: Dict[str, AnyStr] = {}
    files = Path(__file__).parent.glob('*impl')
    for file in files:
        file_name = file.name
        db_name = file_name.split('_')[0]
        db_url = f"{db_name}_url"
        if db_url not in globals(): continue
        db_impl[db_name] = globals()[db_url]
    logger.info(f"The system supports the following databases: {db_impl.keys()}")
    return db_impl

def get_db_impl() -> str:
    """
    获取默认数据库实现
    """
    db_impl = get_all_db_impl().get(config.DATABASE_TYPE, 'mysql')
    if config.DEBUG:
        logger.warning(f"DB config is: {db_impl}")
    logger.info(f"Choice the database type is: {config.DATABASE_TYPE}")
    return db_impl


SQLALCHEMY_DATABASE_URL = get_db_impl()
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


if __name__ == '__main__':
    print(get_db_impl())