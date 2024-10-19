from abc import ABC, abstractmethod
from sqlalchemy.orm import Session
from typing import List, Any, Union
from pydantic import BaseModel


class BaseDBOrm(ABC):
    """
    抽象基类，用于定义数据库操作的基本接口。
    子类应实现所有抽象方法以完成具体的数据库操作。
    """
    model = None
    default_exclude_fields = []

    @classmethod
    def map_to_model(cls, results: Union[List[Any], None, Any]) -> Union[List[BaseModel], BaseModel, None]:
        """
        将查询结果转换为对应的模型实例
        :param results: 查询结果列表
        :return: 模型实例列表
        """

        exclude_fields = set(cls.default_exclude_fields)
        model_columns = cls.model.__table__.columns.keys()
        if not results: return None
        if isinstance(results, list):
            model_instances = []
            for row in results:
                data = {name: value for name, value in zip(model_columns, row) if name not in exclude_fields}
                model_instances.append(cls.model(**data))
            return model_instances
        return cls.model(**{name: value for name, value in zip(model_columns, results) if name not in exclude_fields})


    @classmethod
    @abstractmethod
    def query(cls, db: Session, fields: list=None, many=False, **filters):
        """查询数据，需由子类实现。
        :param db: Session object
        :param fields: return fields
        :param many: return many records
        :param filters: filter
        """
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
