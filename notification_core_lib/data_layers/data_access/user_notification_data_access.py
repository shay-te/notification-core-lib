import logging

from core_lib.connection.sql_alchemy_connection_registry import SqlAlchemyConnectionRegistry
from core_lib.data_layers.data_access.db.crud.crud_data_access import CRUDDataAccess

from notification_core_lib.data_layers.data.db.entities.user_notification import UserNotification


class UserNotificationDataAccess(CRUDDataAccess):

    def __init__(self, db: SqlAlchemyConnectionRegistry):
        super().__init__(UserNotification, db)
        self.logger = logging.getLogger(self.__class__.__name__)
        self._db = db

    def get_by_user(self, user_id: int):
        with self._db.get() as session:
            return session.query(UserNotification).filter(
                UserNotification.user_id == user_id,
            ).first()
