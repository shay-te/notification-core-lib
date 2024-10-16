from core_lib.cache.cache_decorator import Cache
from core_lib.data_layers.service.service import Service
from core_lib.data_transform.result_to_dict import ResultToDict


from notification_core_lib.constants.core_lib_constants import CACHE
from notification_core_lib.data_layers.data.db.entities.user_notification import UserNotification
from notification_core_lib.data_layers.data_access.user_notification_data_access import UserNotificationDataAccess


class UserNotificationService(Service):
    CACHE_USER_NOTIFICATION_ID = 'user_notification_id_{user_id}'

    def __init__(self, user_notification_data_access: UserNotificationDataAccess):
        self._user_notification_data_access = user_notification_data_access

    @Cache(CACHE_USER_NOTIFICATION_ID, handler_name=CACHE)
    @ResultToDict()
    def get_by_user(self, user_id: int):
        return self._user_notification_data_access.get_by_user(user_id)

    @ResultToDict()
    def create(self, user_id: int, notification_id: int):
        return self._user_notification_data_access.create({
            UserNotification.user_id.key: user_id,
            UserNotification.notification_id.key: notification_id,
        })

    @Cache(CACHE_USER_NOTIFICATION_ID, handler_name=CACHE, invalidate=True)
    def update(self, id: int, notification_id: int):
        return self._user_notification_data_access.update(id, {
            UserNotification.notification_id.key: notification_id,
        })

