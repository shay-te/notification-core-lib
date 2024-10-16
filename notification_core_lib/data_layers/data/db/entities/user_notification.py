from datetime import datetime

from sqlalchemy import Column, Integer, INTEGER, DateTime, ForeignKey
from core_lib.data_layers.data.db.sqlalchemy.base import Base


class UserNotification(Base):

    __tablename__ = 'user_notification'

    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(INTEGER, nullable=False)
    notification_id = Column(Integer, ForeignKey('notification.id'), nullable=False)
