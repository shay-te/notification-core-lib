import datetime
import logging

from core_lib.connection.sql_alchemy_connection_registry import SqlAlchemyConnectionRegistry
from core_lib.data_layers.data_access.data_access import DataAccess
from sqlalchemy import cast, or_, Integer, String, text

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

    def all(self, user_id: int, meta_data: dict, project_id: int):
        with self._db.get() as session:
            query = session.query(Notification).filter(
                Notification.project_id == project_id
            )

            user_read_time = session.query(UserNotification.read_at).filter(
                UserNotification.user_id == user_id
            ).one_or_none()
            user_read_time = user_read_time[0]

            if meta_data:
                if meta_data.get('search_string'):
                    search_string = meta_data['search_string']
                    query = query.filter(
                        or_(
                            cast(Notification.meta_data['content'], String).ilike(f'%{search_string}%'),
                            Notification.title.ilike(f"%{search_string}%"),
                        )
                    )
                if meta_data.get('type'):
                    query = query.filter(
                        cast(text("notification.meta_data->>'type'"), Integer) == int(meta_data['type'])
                    )

                if meta_data.get('is_read') is not None and user_read_time:
                    if meta_data['is_read']:
                        query = query.filter(Notification.created_at < user_read_time)
                    else:
                        query = query.filter(Notification.created_at > user_read_time)

            notifications = query.all()
            result = []

            for notification in notifications:
                notification_dict = notification.__dict__.copy()
                notification_dict.pop('_sa_instance_state', None)
                notification_dict[
                 'is_read'] = user_read_time is not None and user_read_time > notification.created_at

            result.append(notification_dict)

            return result



