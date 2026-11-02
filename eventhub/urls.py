
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static

from events import views


urlpatterns = [
    path("admin/", admin.site.urls),

    # Signup and login
    path("signup/", views.signup, name="signup"),

    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="registration/login.html"
        ),
        name="login",
    ),

    path(
        "logout/",
        auth_views.LogoutView.as_view(),
        name="logout",
    ),

    # Dashboard
    path("", views.dashboard, name="dashboard"),

    # Successful Events page
    path(
        "successful-events/",
        views.successful_events,
        name="successful_events",
    ),

    # Create event
    path(
        "event/create/",
        views.event_create,
        name="event_create",
    ),

    # Event details
    path(
        "event/<int:pk>/",
        views.event_detail,
        name="event_detail",
    ),

    # Add task to event
    path(
        "event/<int:pk>/add-task/",
        views.add_task,
        name="add_task",
    ),

    # Delete event
    path(
        "event/<int:pk>/delete/",
        views.delete_event,
        name="delete_event",
    ),

    # Toggle checklist task
    path(
        "task/<int:pk>/toggle/",
        views.toggle_task,
        name="toggle_task",
    ),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
