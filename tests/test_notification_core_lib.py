import unittest
import random
from tests.helpers.utils import sync_create_start_core_lib


class TestNotification(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.notification_core_lib = sync_create_start_core_lib()

    def test_notification(self):
        couple_id = random.randint(1, 1000000)
        project_id = 1
        user_id_1 = random.randint(1, 1000000)
        user_id_2 = random.randint(1, 1000000)

        self.notification_core_lib.notification.create('nfej tification', {'type': 2, 'user_reference_id': '2', 'user_reference_id_2': '54', 'content': 'loremm ipsome'}, project_id)
        self.notification_core_lib.notification.create('new user join app', {'type': 10, 'user_reference_id': '2', 'user_reference_id_2': '44', 'content': ' when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.'}, project_id)
        self.notification_core_lib.notification.create('register complete!', {'type': 1, 'user_reference_id': '14', 'content': 'loremm  fsdfdf fdvdfvg ipsome'}, project_id)
        self.notification_core_lib.notification.create('new match extrnelize', {'type': 10, 'user_reference_id': '2', 'user_reference_id_2': '44', 'content': ' when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.'}, project_id)
        self.notification_core_lib.notification.create('enjoy our new feature', {'type': 10, 'user_reference_id': '2', 'user_reference_id_2': '44', 'content': ' when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.'}, project_id)
        self.notification_core_lib.notification.create('user 123user change his name', {'type': 10, 'user_reference_id': '2', 'user_reference_id_2': '44', 'content': ' when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.'}, project_id)
        self.notification_core_lib.notification.create('some notification', {'type': 10, 'user_reference_id': '2', 'user_reference_id_2': '44', 'content': ' when an unknowt to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.'}, project_id)
        self.notification_core_lib.notification.create('', {'type': 10, 'user_reference_id': '2', 'user_reference_id_2': '44', 'content': ' when an unknowt to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.'}, None)

        self.assertEqual(len(self.notification_core_lib.notification.all(user_id_1, {}, couple_id)), 1)
        self.assertEqual(len(self.notification_core_lib.notification.all(user_id_1, {'a': 1}, couple_id)), 0)
        self.notification_core_lib.notification.create('some notification', {}, couple_id)
        self.assertEqual(len(self.notification_core_lib.notification.all(user_id_1, {}, couple_id)), 1)
        self.assertEqual(len(self.notification_core_lib.notification.all(user_id_1, {'a': 1}, couple_id)), 0)

        self.notification_core_lib.notification.create('some notification', {'a': 1}, couple_id)
        self.assertEqual(len(self.notification_core_lib.notification.all(user_id_1, {}, couple_id)), 2)
        self.assertEqual(len(self.notification_core_lib.notification.all(user_id_1, {'a': 1}, couple_id)), 1)

        self.assertEqual(len(self.notification_core_lib.notification.all(user_id_2, {}, couple_id)), 2)
        self.notification_core_lib.notification.create('some notification', {'b': 'bb'}, couple_id)
        self.assertEqual(len(self.notification_core_lib.notification.all(user_id_2, {'b': 'bb'}, couple_id)), 1)
        self.assertEqual(len(self.notification_core_lib.notification.all(user_id_2, {}, couple_id)), 3)

        self.notification_core_lib.notification.create('some notification', {'a': 1, 'b': 'bb', 'c': [1,2,3]}, couple_id)
        self.assertEqual(len(self.notification_core_lib.notification.all(user_id_2, {'b': 'bb', 'c': [1,2,3]}, couple_id)), 1)
        self.assertEqual(len(self.notification_core_lib.notification.all(user_id_2, {'b': 'bb'}, couple_id)), 2)

        self.notification_core_lib.notification.create('some notification', {'a': 1, 'b': 'bb', 'c': 3.1}, couple_id)
        self.assertEqual(len(self.notification_core_lib.notification.all(user_id_2, {'c': 3.1}, couple_id)), 1)
        self.assertEqual(len(self.notification_core_lib.notification.all(user_id_2, {'a': 1}, couple_id)), 3)

