from django.urls import path
from . import views

urlpatterns = [
    path(
        "",
        views.dashboard,
        name="dashboard",
    ),

    path(
        "signup/",
        views.signup,
        name="signup",
    ),

    path(
        "event/create/",
        views.event_create,
        name="event_create",
    ),

    path(
        "event/<int:pk>/",
        views.event_detail,
        name="event_detail",
    ),

    path(
        "event/<int:pk>/add-task/",
        views.add_task,
        name="add_task",
    ),

    path(
        "task/<int:pk>/toggle/",
        views.toggle_task,
        name="toggle_task",
    ),

    path(
        "event/<int:pk>/delete/",
        views.delete_event,
        name="delete_event",
    ),

    path(
        "successful-events/",
        views.successful_events,
        name="successful_events",
    ),
]