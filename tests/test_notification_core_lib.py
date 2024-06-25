import unittest
import random
from tests.helpers.utils import sync_create_start_core_lib


class TestNotification(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.notification_core_lib = sync_create_start_core_lib()

    def test_notification(self):
        couple_id = random.randint(1, 1000000)
        user_id_1 = random.randint(1, 1000000)
        user_id_2 = random.randint(1, 1000000)
        self.assertEqual(len(self.notification_core_lib.notification.all(user_id_1, {}, couple_id)), 0)
        self.assertEqual(len(self.notification_core_lib.notification.all(user_id_1, {'a': 1}, couple_id)), 0)
        self.notification_core_lib.notification.create('some notification', {}, couple_id)
        self.assertEqual(len(self.notification_core_lib.notification.all(user_id_1, {}, couple_id)), 1)
        self.assertEqual(len(self.notification_core_lib.notification.all(user_id_1, {}, couple_id)), 0)
        self.assertEqual(len(self.notification_core_lib.notification.all(user_id_1, {'a': 1}, couple_id)), 0)

        self.notification_core_lib.notification.create('some notification', {'a': 1}, couple_id)
        self.assertEqual(len(self.notification_core_lib.notification.all(user_id_1, {}, couple_id)), 1)
        self.assertEqual(len(self.notification_core_lib.notification.all(user_id_1, {'a': 1}, couple_id)), 0)

        self.assertEqual(len(self.notification_core_lib.notification.all(user_id_2, {}, couple_id)), 2)
        self.assertEqual(len(self.notification_core_lib.notification.all(user_id_2, {}, couple_id)), 0)
        self.notification_core_lib.notification.create('some notification', {'b': 'bb'}, couple_id)
        self.assertEqual(len(self.notification_core_lib.notification.all(user_id_2, {'b': 'bb'}, couple_id)), 1)
        self.assertEqual(len(self.notification_core_lib.notification.all(user_id_2, {}, couple_id)), 0)

        self.notification_core_lib.notification.create('some notification', {'a': 1, 'b': 'bb', 'c': [1,2,3]}, couple_id)
        self.assertEqual(len(self.notification_core_lib.notification.all(user_id_2, {'b': 'bb'}, couple_id)), 1)
        self.assertEqual(len(self.notification_core_lib.notification.all(user_id_2, {'b': 'bb'}, couple_id)), 0)

        self.notification_core_lib.notification.create('some notification', {'a': 1, 'b': 'bb', 'c': 3.1}, couple_id)
        self.assertEqual(len(self.notification_core_lib.notification.all(user_id_2, {'c': 3.1}, couple_id)), 1)
        self.assertEqual(len(self.notification_core_lib.notification.all(user_id_2, {'c': 3.1}, couple_id)), 0)
