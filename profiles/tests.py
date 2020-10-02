from django.test import TestCase
from django.test.client import Client
from django.shortcuts import reverse
from django.contrib.auth.models import User

# Create your tests here.


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('test', 'test@test.com', 'test1')

    def testLogin(self):
        self.client.login(username='test123', password='test1')
        response = self.client.get(reverse('account_login'))
        self.assertEqual(response.status_code, 200)

