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

    # Pay attention to get all with the correct filter. when you made the query the after_time is neing updates
    # With no matter what params
    @ResultToDict()
    def all(self, user_id: int, meta_data: dict = None, project_id: int = DEFAULT_PROJECT_ID):
        user_notification = self._user_notification_data_access.get(user_id)
        if not user_notification:
            self._user_notification_data_access.create(user_id)
            after_time = datetime.datetime(1970, 1, 1)
        else:
            after_time = user_notification.read_at
            self._user_notification_data_access.update(user_id)
        return self._notification_data_access.all(after_time, meta_data or {}, project_id)

