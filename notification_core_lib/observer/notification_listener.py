from abc import ABC, abstractmethod


class NotificationListener(ABC):

    @abstractmethod
    def notify(self, notification: dict):
        pass
