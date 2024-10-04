
import time
from databases import Base
from datetime import datetime
from utils.time_utils import current_timestamp
from sqlalchemy import Column, String, Boolean, DateTime, BigInteger





class BaseModel(Base):
    """
    基础model
    """
    __abstract__ = True
    id = Column(BigInteger, primary_key=True)
    create_time = Column(BigInteger, nullable=True, index=True, comment="create time | 创建时间，时间戳格式", default=current_timestamp)
    create_date = Column(DateTime, nullable=True, index=True, comment="create date | 创建日期，日期格式", default=datetime.now)
    update_time = Column(BigInteger, nullable=True, index=True, comment="update time | 更新时间，时间戳格式", default=current_timestamp)
    update_date = Column(DateTime, nullable=True, index=True, comment="update date | 更新日期，日期格式", default=datetime.now)
    created_by = Column(String(32), nullable=True, index=True, comment="created by | 创建人")
    is_deleted = Column(Boolean, default=False, comment="is deleted | 是否已删除")