import datetime
import logging

from core_lib.connection.sql_alchemy_connection_registry import SqlAlchemyConnectionRegistry
from core_lib.data_layers.data_access.data_access import DataAccess

from notification_core_lib.data_layers.data.db.entities.user_notification import UserNotification


class UserNotificationDataAccess(DataAccess):

    def __init__(self, db: SqlAlchemyConnectionRegistry):
        self.logger = logging.getLogger(self.__class__.__name__)
        self._db = db

    def create(self, user_id: int):
        with self._db.get() as session:
            notification = UserNotification()
            notification.user_id = user_id
            notification.read_at = datetime.datetime.utcnow()
            session.add(notification)
        return notification

    def get(self, user_id: int):
        with self._db.get() as session:
            return session.query(UserNotification) \
                   .filter(UserNotification.user_id == user_id) \
                   .first()

    def update(self, user_id: int):
        with self._db.get() as session:
            return session.query(UserNotification) \
                   .filter(UserNotification.user_id == user_id) \
                   .update({UserNotification.read_at: datetime.datetime.utcnow()})
