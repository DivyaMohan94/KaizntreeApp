from rest_framework.test import APITestCase
from django.urls import reverse


class TestSetUp(APITestCase):

    def setUp(self):
        self.register_url = reverse('signup')
        self.login_url = reverse('login')

        self.user_data = {
            'username': "johndoe",
            'email': "johndoe@gmail.com",
            'password': "1234567",
        }

    def tearDown(self):
        return super().tearDown()