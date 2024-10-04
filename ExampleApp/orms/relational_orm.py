import inspect
from common.logger import logger
from ExampleApp.orms.base import BaseDBOrm
from utils.meta_utils import print_current_function_module
from sqlalchemy.orm import Session


class RelationalDBOrm(BaseDBOrm):
    """
    关系型数据库ORM（对象关系映射）类
    该类提供与关系型数据库（如 MySQL、PostgresSQL 等）交互的基本方法。
    子类需要实现这些方法以提供具体的数据库操作。
    """

    model = None  # 定义 ORM 模型类，子类应将其设置为对应的模型

    @classmethod
    def query(cls):
        """
        查询数据的方法。
        该方法应根据具体的数据库逻辑实现数据查询功能。
        :return: 查询结果
        """

        pass

    @classmethod
    def save(cls, db: Session, **kwargs):
        """
        保存数据的方法。
        该方法应处理数据的保存操作，并根据需要决定是插入新记录还是更新现有记录。
        :param kwargs: 需要保存的数据字段
        :param db: session object
        :return: 保存结果，通常是保存的对象或状态信息
        """
        _model = cls.model(**kwargs)
        db.add(_model)
        db.commit()
        db.refresh(_model)

    @classmethod
    def insert(cls, **kwargs):
        """
        插入数据的方法。
        该方法应处理新数据的插入操作。
        :param kwargs: 需要插入的数据字段
        :return: 插入结果，通常是插入的对象或状态信息
        """
        pass

    @classmethod
    def update(cls, **kwargs):
        """
        更新数据的方法。
        该方法应处理现有记录的更新操作。
        :param kwargs: 需要更新的数据字段及条件
        :return: 更新结果，通常是更新的对象或状态信息
        """
        pass

    @classmethod
    def delete_by_id(cls, pid: int):
        """
        根据 ID 删除数据的方法。
        该方法应处理根据给定 ID 删除数据库记录的操作。
        :param pid: 要删除记录的 ID
        :return: 删除结果，通常是删除的状态信息
        """
        pass

    @classmethod
    def delete_by_ids(cls, pids: list):
        """
        根据多个 ID 删除数据的方法。
        该方法应处理根据给定 ID 列表删除数据库记录的操作。
        :param pids: 要删除记录的 ID 列表
        :return: 删除结果，通常是删除的状态信息
        """
        pass

    @classmethod
    def test_print(cls):
        """
        测试 test_print 方法被执行...
        :param cls: 类自身
        :return: None
        """
        print_current_function_module()
