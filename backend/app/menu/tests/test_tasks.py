from django.test import TestCase
from mixer.backend.django import mixer
from parameterized import parameterized
from unittest import mock
from django.core import mail

from menu.tasks import MenuTask
from .mocks.task_mocks import SEND_NOTIFICATION_TASK


class TestTasks(TestCase):

    @parameterized.expand(SEND_NOTIFICATION_TASK)
    @mock.patch('menu.tasks.datetime')
    def test__send_notification_with_updated_data(self, dishes, datetime_now, users, should_send, message_to,
                                                  mocked_datetime):
        mocked_datetime.now.return_value = datetime_now

        for dish in dishes:
            with mock.patch('django.utils.timezone.now', mock.Mock(return_value=dish['create_date'])):
                dish_obj = mixer.blend('menu.Dish', **dish)

                if 'last_update_date' in dish:
                    with mock.patch('django.utils.timezone.now', mock.Mock(return_value=dish['last_update_date'])):
                        dish_obj.name = 'test'
                        dish_obj.save()

        for user in users:
            mixer.blend('auth.User', **user)

        result = MenuTask.send_notification_with_updated_data()
        if should_send:
            self.assertEqual(len(mail.outbox), 1)
            self.assertEqual(mail.outbox[0].subject, 'Updated Menus')
            self.assertEqual(mail.outbox[0].to, message_to)
        else:
            self.assertEqual(len(mail.outbox), 0)
            self.assertEqual(result, "Nothing has been changed")
