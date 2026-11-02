
from django.contrib import admin

from .models import Event, Task


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'event_type', 'date', 'time', 'venue', 'created_by')
    list_filter = ('event_type', 'date')
    search_fields = ('title', 'description', 'venue')


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'event', 'assigned_to', 'deadline', 'done')
    list_filter = ('done', 'deadline')
    search_fields = ('title',)