from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APITestCase

from .models import Task


class TaskAPITest(APITestCase):

    def setUp(self):

        self.user = User.objects.create_user(
            username="navaneeth",
            password="password123",
        )

        response = self.client.post(
            "/api/login/",
            {
                "username": "navaneeth",
                "password": "password123",
            },
        )

        self.token = response.data["access"]

        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {self.token}"
        )

    def test_create_task(self):

        response = self.client.post(
            "/api/tasks/",
            {
                "title": "Learn GitHub Actions",
                "description": "Finish CI module",
            },
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
        )

        self.assertEqual(
            Task.objects.count(),
            1,
        )

    def test_list_tasks(self):

        Task.objects.create(
            user=self.user,
            title="Task 1",
        )

        Task.objects.create(
            user=self.user,
            title="Task 2",
        )

        response = self.client.get("/api/tasks/")

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        self.assertEqual(
            len(response.data),
            2,
        )

    def test_retrieve_task(self):

        task = Task.objects.create(
            user=self.user,
            title="Learn Docker",
        )

        response = self.client.get(
            f"/api/tasks/{task.id}/"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        self.assertEqual(
            response.data["title"],
            "Learn Docker",
        )

    def test_update_task(self):

        task = Task.objects.create(
            user=self.user,
            title="Old Title",
        )

        response = self.client.put(
            f"/api/tasks/{task.id}/",
            {
                "title": "New Title",
                "description": "",
                "completed": True,
            },
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        task.refresh_from_db()

        self.assertEqual(
            task.title,
            "New Title",
        )

        self.assertTrue(
            task.completed
        )

    def test_delete_task(self):

        task = Task.objects.create(
            user=self.user,
            title="Delete Me",
        )

        response = self.client.delete(
            f"/api/tasks/{task.id}/"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT,
        )

        self.assertEqual(
            Task.objects.count(),
            0,
        )

    def test_user_can_only_see_own_tasks(self):

        another_user = User.objects.create_user(
            username="john",
            password="password123",
        )

        Task.objects.create(
            user=self.user,
            title="My Task",
        )

        Task.objects.create(
            user=another_user,
            title="John Task",
        )

        response = self.client.get("/api/tasks/")

        self.assertEqual(
            len(response.data),
            1,
        )

        self.assertEqual(
            response.data[0]["title"],
            "My Task",
        )
    
    def test_unauthenticated_user_cannot_access_tasks(self):

        self.client.credentials()

        response = self.client.get("/api/tasks/")

        self.assertEqual(
            response.status_code,
            status.HTTP_401_UNAUTHORIZED,
        )