import json

from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from mixer.backend.django import mixer


class PermissionTestCase(TestCase):
    def setUp(self):
        super().setUp()
        self.user1 = User.objects.create(username='test', password='test', is_superuser=True, is_staff=True)
        self.user2 = User.objects.create(username='test1', password='test')

        self.dish1 = mixer.blend('menu.Dish')
        self.dish2 = mixer.blend('menu.Dish')
        self.dish3 = mixer.blend('menu.Dish')
        self.dish4 = mixer.blend('menu.Dish')

        self.menu1 = mixer.blend('menu.MenuCard', dishes=[self.dish1.pk, self.dish2.pk])
        self.menu2 = mixer.blend('menu.MenuCard', dishes=[self.dish2.pk, self.dish3.pk])
        self.menu3 = mixer.blend('menu.MenuCard', dishes=[self.dish3.pk, self.dish1.pk])
        self.menu4 = mixer.blend('menu.MenuCard', dishes=[self.dish2.pk, self.dish4.pk])
        self.menu5 = mixer.blend('menu.MenuCard', dishes=[])

    def test__permission_get_card_menu(self):
        client = APIClient()
        response = client.get('/menu-cards/')

        status_code = response.status_code
        content = json.loads(response.content)

        self.assertEqual(status_code, 200)
        self.assertEqual(content['count'], 4)

    def test__permission_get_card_menu_details(self):
        client = APIClient()

        response = client.get(f'/menu-cards/{str(self.menu1.pk)}/')
        status_code = response.status_code
        self.assertEqual(status_code, 200)

        response = client.get(f'/menu-cards/{str(self.menu2.pk)}/')
        status_code = response.status_code
        self.assertEqual(status_code, 200)

        response = client.get(f'/menu-cards/{str(self.menu3.pk)}/')
        status_code = response.status_code
        self.assertEqual(status_code, 200)

        response = client.get(f'/menu-cards/{str(self.menu4.pk)}/')
        status_code = response.status_code
        self.assertEqual(status_code, 200)

        response = client.get(f'/menu-cards/{str(self.menu5.pk)}/')
        status_code = response.status_code
        self.assertEqual(status_code, 404)

    def test__permission_post_card_menu_details(self):
        client = APIClient()

        data = {'name': 'test', 'description': 'test', 'dishes': [self.dish2.pk,]}
        response = client.post(f'/menu-cards/', data=data)
        status_code = response.status_code
        self.assertEqual(status_code, 401)

        client.force_authenticate(user=self.user1)
        request = client.post(f'/menu-cards/', data=data)
        status_code = request.status_code
        self.assertEqual(status_code, 201)

    def test__permission_put_card_menu_details(self):
        client = APIClient()

        data = {'name': 'test12', 'description': 'test', 'dishes': [self.dish2.pk, ]}
        response = client.put(f'/menu-cards/{str(self.menu1.pk)}/', data=data)
        status_code = response.status_code
        self.assertEqual(status_code, 401)

        client.force_authenticate(user=self.user1)
        response = client.put(f'/menu-cards/{str(self.menu1.pk)}/', data=data)
        status_code = response.status_code
        self.assertEqual(status_code, 200)

    def test__permission_patch_card_menu_details(self):
        client = APIClient()

        data = {'description': 'test12'}
        response = client.patch(f'/menu-cards/{str(self.menu1.pk)}/', data=data)
        status_code = response.status_code
        self.assertEqual(status_code, 401)

        client.force_authenticate(user=self.user1)
        response = client.patch(f'/menu-cards/{str(self.menu1.pk)}/', data=data)
        status_code = response.status_code
        self.assertEqual(status_code, 200)

    def test__permission_delete_card_menu_details(self):
        client = APIClient()

        response = client.delete(f'/menu-cards/{str(self.menu1.pk)}/')
        status_code = response.status_code
        self.assertEqual(status_code, 401)

        client.force_authenticate(user=self.user1)
        response = client.delete(f'/menu-cards/{str(self.menu1.pk)}/')
        status_code = response.status_code
        self.assertEqual(status_code, 204)