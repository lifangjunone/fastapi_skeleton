from ExampleApp.orms.base import BaseDBOrm
from utils.meta_utils import print_current_function_module


class NoSQLDBOrm(BaseDBOrm):
    """
    非关系型数据库ORM（对象关系映射）类
    该类提供与非关系型数据库（如 MongoDB 等）交互的基本方法。
    子类需要实现这些方法以提供具体的数据库操作。
    """

    model = None  # 定义 ORM 模型类，子类应将其设置为对应的模型

    @classmethod
    def query(cls):
        """
        查询数据的方法。
        该方法应根据具体的数据库逻辑实现数据查询功能。
        :return: 查询结果，通常是符合查询条件的文档列表或对象
        """
        pass

    @classmethod
    def save(cls, **kwargs):
        """
        保存数据的方法。
        该方法应处理数据的保存操作，决定是插入新文档还是更新现有文档。
        :param kwargs: 需要保存的数据字段
        :return: 保存结果，通常是保存的文档或状态信息
        """
        pass

    @classmethod
    def insert(cls, **kwargs):
        """
        插入数据的方法。
        该方法应处理新文档的插入操作。
        :param kwargs: 需要插入的数据字段
        :return: 插入结果，通常是插入的文档或状态信息
        """
        pass

    @classmethod
    def update(cls, **kwargs):
        """
        更新数据的方法。
        该方法应处理现有文档的更新操作。
        :param kwargs: 需要更新的数据字段及条件
        :return: 更新结果，通常是更新的文档或状态信息
        """
        pass

    @classmethod
    def delete_by_id(cls, pid: int):
        """
        根据 ID 删除数据的方法。
        该方法应处理根据给定 ID 删除数据库文档的操作。
        :param pid: 要删除文档的 ID
        :return: 删除结果，通常是删除的状态信息
        """
        pass

    @classmethod
    def delete_by_ids(cls, pids: list):
        """
        根据多个 ID 删除数据的方法。
        该方法应处理根据给定 ID 列表删除数据库文档的操作。
        :param pids: 要删除文档的 ID 列表
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
