
from django.db import models
from django.contrib.auth.models import User


# --------------------------------------------------
# EVENT MODEL
# --------------------------------------------------

class Event(models.Model):

    title = models.CharField(
        max_length=200
    )

    description = models.TextField(
        blank=True
    )

    date = models.DateField()

    time = models.TimeField(
        null=True,
        blank=True
    )

    venue = models.CharField(
        max_length=200,
        blank=True
    )

    event_type = models.CharField(
        max_length=50,
        blank=True
    )

    upload = models.FileField(
        upload_to="uploads/",
        blank=True
    )

    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="created_events"
    )

    class Meta:
        ordering = ["date"]

    def __str__(self):
        return self.title

    # Calculate checklist progress
    def progress(self):

        total = self.tasks.count()

        done = self.tasks.filter(
            done=True
        ).count()

        return done, total


# --------------------------------------------------
# TASK MODEL
# --------------------------------------------------

class Task(models.Model):

    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name="tasks"
    )

    title = models.CharField(
        max_length=200
    )

    # Any person's name can be entered
    assigned_to = models.CharField(
        max_length=100,
        blank=True,
        default=""
    )

    deadline = models.DateField(
        null=True,
        blank=True
    )

    done = models.BooleanField(
        default=False
    )

    class Meta:
        ordering = ["deadline", "id"]

    def __str__(self):
        return self.title
