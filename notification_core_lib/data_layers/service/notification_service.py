from core_lib.data_layers.service.service import Service
from core_lib.data_transform.result_to_dict import ResultToDict
from notification_core_lib.constants.core_lib_constants import DEFAULT_PROJECT_ID

from notification_core_lib.data_layers.data.db.entities.notification import Notification
from notification_core_lib.data_layers.data.db.entities.user_notification import UserNotification
from notification_core_lib.data_layers.data_access.notification_data_access import NotificationDataAccess
from notification_core_lib.data_layers.service.user_notification_service import UserNotificationService


class NotificationService(Service):

    def __init__(self,
                 notification_data_access: NotificationDataAccess,
                 user_notification_service: UserNotificationService):
        self._notification_data_access = notification_data_access
        self._user_notification_service = user_notification_service

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
        last_read_notification = self._user_notification_service.get_by_user(user_id)
        if last_read_notification:
            if last_read_notification[UserNotification.notification_id.key] < notification_id:
                self._user_notification_service.update(last_read_notification[UserNotification.id.key], notification_id)
        else:
            self._user_notification_service.create(user_id, notification_id)
