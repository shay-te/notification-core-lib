from sqlalchemy import Column, Integer, INTEGER, ForeignKey, Index
from core_lib.data_layers.data.db.sqlalchemy.base import Base


class UserNotification(Base):

    __tablename__ = 'user_notification'

    INDEX_USER_ID = 'user_notification_user_id'

    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(INTEGER, nullable=False)
    notification_id = Column(Integer, ForeignKey('notification.id'), nullable=False)

    Index(INDEX_USER_ID, 'user_id', unique=True),
