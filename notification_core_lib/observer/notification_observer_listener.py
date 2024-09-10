from core_lib.observer.observer_listener import ObserverListener

from notification_core_lib.observer.notification_listener import NotificationListener


class NotificationObserverListener(ObserverListener):
    EVENT_NOTIFICATION_CREATED = 'EVENT_NOTIFICATION_CREATED'

    def __init__(self, notification_completion_cb: NotificationListener):
        self._notification_completion_cb = notification_completion_cb

    def update(self, key: str, value):
        if key == NotificationObserverListener.EVENT_NOTIFICATION_CREATED:
            self._notification_completion_cb.notify(value['name'])
