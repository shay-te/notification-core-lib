import unittest
import random
from tests.helpers.utils import sync_create_start_core_lib


class TestNotification(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.notification_core_lib = sync_create_start_core_lib()

    def test_notification(self):
        project_id = random.randint(2000, 1000000)

        self.notification_core_lib.notification.create('nfej tification', {'type': 2, 'user_reference_id': '2', 'user_reference_id_2': '54', 'content': 'loremm ipsome'}, project_id)
        self.notification_core_lib.notification.create('new user join app', {'type': 10, 'user_reference_id': '2', 'user_reference_id_2': '44', 'content': ' when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.'}, project_id)
        self.notification_core_lib.notification.create('register complete!', {'type': 1, 'user_reference_id': '14', 'content': 'loremm  fsdfdf fdvdfvg ipsome'}, project_id)
        self.notification_core_lib.notification.create('new match extrnelize', {'type': 10, 'user_reference_id': '2', 'user_reference_id_2': '44', 'content': ' when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.'}, project_id)
        self.notification_core_lib.notification.create('enjoy our new feature', {'type': 10, 'user_reference_id': '2', 'user_reference_id_2': '44', 'content': ' when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.'}, project_id)
        self.notification_core_lib.notification.create('user 123user change his name', {'type': 10, 'user_reference_id': '2', 'user_reference_id_2': '44', 'content': ' when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.'}, project_id)
        self.notification_core_lib.notification.create('some notification', {'type': 10, 'user_reference_id': '2', 'user_reference_id_2': '44', 'content': ' when an unknowt to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.'}, project_id)
        self.notification_core_lib.notification.create('', {'type': 10, 'user_reference_id': '2', 'user_reference_id_2': '44', 'content': ' when an unknowt to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.'}, project_id)

        self.assertEqual(len(self.notification_core_lib.notification.all(None, {}, project_id)), 8)
        self.assertEqual(len(self.notification_core_lib.notification.all(None, {'a': 1}, project_id)), 0)
        self.notification_core_lib.notification.create('some notification', {}, project_id)
        self.assertEqual(len(self.notification_core_lib.notification.all(None, {'type': 10}, project_id)), 6)
        self.assertEqual(len(self.notification_core_lib.notification.all('user', {'type': 10}, project_id)), 2)





