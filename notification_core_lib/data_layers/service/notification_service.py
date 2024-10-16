import datetime

from core_lib.data_layers.service.service import Service
from core_lib.data_transform.result_to_dict import ResultToDict

from notification_core_lib.constants import DEFAULT_PROJECT_ID
from notification_core_lib.data_layers.data.db.entities.notification import Notification
from notification_core_lib.data_layers.data.db.entities.user_notification import UserNotification
from notification_core_lib.data_layers.data_access.notification_data_access import NotificationDataAccess
from notification_core_lib.data_layers.data_access.user_notification_data_access import UserNotificationDataAccess


class NotificationService(Service):

    def __init__(self,
                 notification_data_access: NotificationDataAccess,
                 user_notification_data_access: UserNotificationDataAccess):
        self._notification_data_access = notification_data_access
        self._user_notification_data_access = user_notification_data_access

    @ResultToDict()
    def create(self, title, meta_data: dict, project_id: int = DEFAULT_PROJECT_ID):
        return self._notification_data_access.create({
            Notification.title.key: title,
            Notification.meta_data.key: meta_data,
            Notification.project_id.key: project_id
        })

    @ResultToDict()
    def all(self, title: str = None, meta_data: dict = None, user_id: int = None, project_id: int = DEFAULT_PROJECT_ID):
        notifications = self._notification_data_access.all(title, meta_data, user_id, project_id)
        return notifications

    def read(self, user_id: int, notification_id: int):
        self._user_notification_data_access.read(user_id, notification_id)
