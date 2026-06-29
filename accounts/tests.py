from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase


class RegisterAPITest(APITestCase):

    def test_user_registration(self):

        url = "/api/register/"

        data = {
            "username": "navaneeth",
            "email": "nav@example.com",
            "password": "password123",
        }

        response = self.client.post(url, data)

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
        )

        self.assertEqual(
            User.objects.count(),
            1,
        )

        self.assertEqual(
            User.objects.get().username,
            "navaneeth",
        )

        self.assertTrue(
            User.objects.get().check_password("password123")
        )