from core_lib.core_lib_listener import CoreLibListener
from core_lib.observer.observer import Observer
from omegaconf import DictConfig
import os
import inspect
from core_lib.alembic.alembic import Alembic
from core_lib.core_lib import CoreLib
from core_lib.cache.cache_handler_memcached import CacheHandlerMemcached
from core_lib.data_layers.data.data_helpers import build_url
from core_lib.connection.sql_alchemy_connection_registry import SqlAlchemyConnectionRegistry

from notification_core_lib.data_layers.data_access.notification_data_access import NotificationDataAccess
from notification_core_lib.data_layers.data_access.user_notification_data_access import UserNotificationDataAccess
from notification_core_lib.data_layers.service.notification_service import NotificationService
from notification_core_lib.observer.notification_listener import NotificationListener


class NotificationCoreLib(CoreLib):
    def __init__(self, conf: DictConfig):
        super().__init__()
        self.config = conf

        CoreLib.cache_registry.register('notification', CacheHandlerMemcached(build_url(**self.config.core_lib.notification_core_lib.cache.notification.url)))
        db = SqlAlchemyConnectionRegistry(self.config.core_lib.data.sqlalchemy)
        self.notification = NotificationService(NotificationDataAccess(db), UserNotificationDataAccess(db))
        self.notification_observer = Observer()

    def attach_notification_listener(self, notification_server_listener:NotificationListener):
        from notification_core_lib.observer.notification_observer_listener import NotificationObserverListener
        self.notification_observer.attach(NotificationObserverListener(notification_server_listener))

    @staticmethod
    def install(cfg: DictConfig):
        Alembic(os.path.dirname(inspect.getfile(NotificationCoreLib)), cfg).upgrade()

    @staticmethod
    def uninstall(cfg: DictConfig):
        Alembic(os.path.dirname(inspect.getfile(NotificationCoreLib)), cfg).downgrade()
