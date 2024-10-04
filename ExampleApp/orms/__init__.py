from pathlib import Path
from conf.default import config
from common.logger import logger
from typing import Dict, AnyStr, Any
from ExampleApp.orms.base import BaseDBOrm
from ExampleApp.orms.nosql_orm import NoSQLDBOrm as nosql_orm
from ExampleApp.orms.relational_orm import RelationalDBOrm as relational_orm


def get_all_orm_impl():
    """
    获取所有的orm实现
    """
    orm_impl: Dict[str, Any] = {}
    files = Path(__file__).parent.glob('*orm.py')
    for file in files:
        file_name = file.name
        orm_name = file_name.split('.')[0]
        if orm_name not in globals(): continue
        orm_impl[orm_name] = globals()[orm_name]
    logger.info(f"The system supports the following orm: {orm_impl.keys()}")
    return orm_impl


def get_orm_impl() -> BaseDBOrm:
    """
    获取默认的orm实现
    """
    system_orm = config.ORM_TYPE
    if not system_orm.endswith("_orm"):
        system_orm += "_orm"
    orm_impl = get_all_orm_impl().get(system_orm, 'relational_orm')
    if config.DEBUG:
        logger.warning(f"ORM impl is: {orm_impl}")
    logger.info(f"Choice the orm type is: {system_orm}")
    return orm_impl


if __name__ == '__main__':
    print(get_orm_impl())