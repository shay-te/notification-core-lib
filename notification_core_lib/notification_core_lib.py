from omegaconf import DictConfig
import os
import inspect
from core_lib.alembic.alembic import Alembic
from core_lib.core_lib import CoreLib
from core_lib.cache.cache_handler_memcached import CacheHandlerMemcached
from core_lib.data_layers.data.data_helpers import build_url
from core_lib.connection.sql_alchemy_connection_registry import SqlAlchemyConnectionRegistry
from core_lib.observer.observer import Observer
from notification_core_lib.constants.core_lib_constants import CACHE, NOTIFICATION_CORE_LIB_NAME

from notification_core_lib.data_layers.data_access.notification_data_access import NotificationDataAccess
from notification_core_lib.data_layers.data_access.user_notification_data_access import UserNotificationDataAccess
from notification_core_lib.data_layers.service.notification_service import NotificationService
from notification_core_lib.data_layers.service.user_notification_service import UserNotificationService
from notification_core_lib.observer.notification_listener import NotificationListener
from notification_core_lib.observer.notification_observer_listener import NotificationObserverListener


class NotificationCoreLib(CoreLib):
    def __init__(self, conf: DictConfig):
        super().__init__()
        self.config = conf

        CoreLib.cache_registry.register(CACHE, CacheHandlerMemcached(build_url(**self.config.core_lib.notification_core_lib.cache.notification.url)))
        db = SqlAlchemyConnectionRegistry(self.config.core_lib.data.sqlalchemy)
        self.notification = NotificationService(
            NotificationDataAccess(db),
            UserNotificationService(UserNotificationDataAccess(db))
        )

        self._notification_observer = Observer()
        CoreLib.observer_registry.register(NOTIFICATION_CORE_LIB_NAME, self._notification_observer)

    def attach_notification_listener(self, notification_listener: NotificationListener):
        assert notification_listener is not None and isinstance(notification_listener, NotificationListener)
        self._notification_observer.attach(NotificationObserverListener(notification_listener))

    @staticmethod
    def install(cfg: DictConfig):
        Alembic(os.path.dirname(inspect.getfile(NotificationCoreLib)), cfg).upgrade()

    @staticmethod
    def uninstall(cfg: DictConfig):
        Alembic(os.path.dirname(inspect.getfile(NotificationCoreLib)), cfg).downgrade()
