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


class LoginAPITest(APITestCase):

    def setUp(self):

        User.objects.create_user(
            username="navaneeth",
            password="password123",
        )

    def test_login_success(self):

        url = "/api/login/"

        data = {
            "username": "navaneeth",
            "password": "password123",
        }

        response = self.client.post(url, data)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        self.assertIn(
            "access",
            response.data,
        )

        self.assertIn(
            "refresh",
            response.data,
        )
    
    def test_login_invalid_credentials(self):

        url = "/api/login/"

        data = {
            "username": "navaneeth",
            "password": "wrongpassword",
        }   

        response = self.client.post(url, data)

        self.assertEqual(
            response.status_code,
            status.HTTP_401_UNAUTHORIZED,
        )