from abc import ABC, abstractmethod
from sqlalchemy.orm import Session


class BaseDBOrm(ABC):
    """
    抽象基类，用于定义数据库操作的基本接口。
    子类应实现所有抽象方法以完成具体的数据库操作。
    """
    model = None

    @classmethod
    @abstractmethod
    def query(cls):
        """查询数据，需由子类实现。"""
        pass

    @classmethod
    @abstractmethod
    def save(cls, db: Session, **kwargs):
        """保存数据，需由子类实现。
        :param db: Session object
        :param kwargs: model attributes
        """
        pass

    @classmethod
    @abstractmethod
    def insert(cls, **kwargs):
        """插入数据，需由子类实现。"""
        pass

    @classmethod
    @abstractmethod
    def update(cls, **kwargs):
        """更新数据，需由子类实现。"""
        pass

    @classmethod
    @abstractmethod
    def delete_by_id(cls, pid: int):
        """根据 ID 删除数据，需由子类实现。"""
        pass

    @classmethod
    @abstractmethod
    def delete_by_ids(cls, pids: list):
        """根据多个 ID 删除数据，需由子类实现。"""
        pass

    @classmethod
    @abstractmethod
    def test_print(cls):
        """
        测试打印
        """
        raise NotImplemented
