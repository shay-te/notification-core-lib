import logging

from core_lib.connection.sql_alchemy_connection_registry import SqlAlchemyConnectionRegistry
from core_lib.data_layers.data_access.db.crud.crud_data_access import CRUDDataAccess

from notification_core_lib.data_layers.data.db.entities.user_notification import UserNotification


class UserNotificationDataAccess(CRUDDataAccess):

    def __init__(self, db: SqlAlchemyConnectionRegistry):
        super().__init__(UserNotification, db)
        self.logger = logging.getLogger(self.__class__.__name__)
        self._db = db

    def read(self, user_id: int, notification_id: int):
        field = None
        with self._db.get() as session:
            existing_value = session.query(UserNotification) \
                .filter(
                UserNotification.user_id == user_id,
            ).first()
            if existing_value:
                existing_value.notification_id = notification_id
                field = existing_value
            else:
                user_notification = UserNotification()
                user_notification.user_id = user_id
                user_notification.notification_id = notification_id
                session.add(user_notification)
                session.commit()
                field = user_notification
        return field
