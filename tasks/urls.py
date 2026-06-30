from django.urls import path

from .views import TaskCreateView

urlpatterns = [
    path(
        "tasks/",
        TaskCreateView.as_view(),
        name="task-create",
    ),
]