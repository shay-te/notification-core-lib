import datetime

from core_lib.data_layers.service.service import Service
from core_lib.data_transform.result_to_dict import ResultToDict

from notification_core_lib.constants import DEFAULT_PROJECT_ID
from notification_core_lib.data_layers.data_access.notification_data_access import NotificationDataAccess
from notification_core_lib.data_layers.data_access.user_notification_data_access import UserNotificationDataAccess


class NotificationService(Service):

    def __init__(self, notification_data_access: NotificationDataAccess,
                 user_notification_data_access: UserNotificationDataAccess):
        self._notification_data_access = notification_data_access
        self._user_notification_data_access = user_notification_data_access

    @ResultToDict()
    def create(self, title, meta_data: dict, project_id: int = DEFAULT_PROJECT_ID):
        return self._notification_data_access.create(title, meta_data, project_id)

    @ResultToDict()
    def all(self, title: str = None, meta_data: dict = None, project_id: int = DEFAULT_PROJECT_ID):
        notifications = self._notification_data_access.all(title, meta_data, project_id)
        return notifications
