import logging

from core_lib.connection.sql_alchemy_connection_registry import SqlAlchemyConnectionRegistry
from sqlalchemy import cast, case, and_
from sqlalchemy.dialects.postgresql import JSONB

from core_lib.data_layers.data_access.db.crud.crud_soft_data_access import CRUDSoftDeleteDataAccess
from notification_core_lib.data_layers.data.db.entities.notification import Notification
from notification_core_lib.data_layers.data.db.entities.user_notification import UserNotification


class NotificationDataAccess(CRUDSoftDeleteDataAccess):

    def __init__(self, db: SqlAlchemyConnectionRegistry):
        super().__init__(Notification, db)
        self.logger = logging.getLogger(self.__class__.__name__)
        self._db = db

    def all(self, title: str, meta_data: dict, user_id: int, project_id: int):
        with self._db.get() as session:
            query = session.query(
                *list(Notification.__table__.columns),
                case(
                    [
                        (Notification.id > UserNotification.notification_id, False)
                    ],
                    else_=True
                ).label('is_read')
            ).outerjoin(
                UserNotification,
                and_(
                    UserNotification.user_id == user_id,
                    UserNotification.notification_id.isnot(None)
                )
            ).filter(Notification.project_id == project_id)

            if title:
                query = query.filter(Notification.title.ilike(f'%{title}%'))
            if meta_data:
                query = query.filter(cast(Notification.meta_data, JSONB).contains(meta_data))

            return query.order_by(Notification.id.desc()).all()
