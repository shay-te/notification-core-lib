import unittest
import random

from notification_core_lib.data_layers.data.db.entities.notification import Notification
from notification_core_lib.data_layers.data.db.entities.user_notification import UserNotification
from tests.helpers.utils import sync_create_start_core_lib


class TestDeleteByProjectId(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.notification_core_lib = sync_create_start_core_lib()

    def test_delete_by_project_id(self):
        project_id = random.randint(2000, 1000000)
        user_id = random.randint(2000, 1000000)

        self.notification_core_lib.notification.create('first notification', {'type': 1}, project_id)
        notification = self.notification_core_lib.notification.create('second notification', {'type': 2}, project_id)
        self.notification_core_lib.notification.read(user_id, notification['id'])

        self.notification_core_lib.notification.delete_by_project_id(project_id)

        db = self.notification_core_lib.notification._notification_data_access._db
        with db.get() as session:
            active_notifications = session.query(Notification).filter(
                Notification.deleted_at.is_(None),
                Notification.project_id == project_id
            ).count()
            self.assertEqual(active_notifications, 0)

            remaining_user_notifications = session.query(UserNotification).filter(
                UserNotification.user_id == user_id
            ).count()
            self.assertEqual(remaining_user_notifications, 0)
