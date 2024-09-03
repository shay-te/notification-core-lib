import datetime
import logging

from core_lib.connection.sql_alchemy_connection_registry import SqlAlchemyConnectionRegistry
from core_lib.data_layers.data_access.data_access import DataAccess
from sqlalchemy import cast, or_, Integer, String, text, func
from sqlalchemy.dialects.postgresql import JSONB

from notification_core_lib.data_layers.data.db.entities.notification import Notification
from notification_core_lib.data_layers.data.db.entities.user_notification import UserNotification


class NotificationDataAccess(DataAccess):

    def __init__(self, db: SqlAlchemyConnectionRegistry):
        self.logger = logging.getLogger(self.__class__.__name__)
        self._db = db

    def create(self, title: str, meta_data: dict, project_id: int):
        with self._db.get() as session:
            notification = Notification()
            notification.title = title
            notification.meta_data = meta_data
            notification.project_id = project_id
            session.add(notification)
        return notification

    def all(self, meta_data: dict, user_license: list, project_id: int):
        with self._db.get() as session:
            query = session.query(Notification).filter(
                Notification.project_id == project_id
            )

            if meta_data:
                query = query.filter(cast(Notification.meta_data, JSONB).contains(meta_data))

            # if user_license:
            #     query = query.filter(
            #         cast(Notification.meta_data['modules'], JSONB).overlap(user_license)
            #     )

            return query.all()

