import datetime
import logging

from core_lib.connection.sql_alchemy_connection_registry import SqlAlchemyConnectionRegistry
from core_lib.data_layers.data_access.data_access import DataAccess
from core_lib.data_layers.data_access.db.db_data_helpers import sqlalchemy_filter_query_by_meta_data

from notification_core_lib.data_layers.data.db.entities.notification import Notification


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

    def all(self, after_time: datetime.datetime, meta_data: dict, project_id: int):
        with self._db.get() as session:
            query = session.query(Notification)
            if meta_data:
                query = sqlalchemy_filter_query_by_meta_data(Notification, Notification.meta_data.key, query, meta_data)
            return query.filter(Notification.created_at > after_time, Notification.project_id == project_id).all()
