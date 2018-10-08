from django.contrib import admin
from .models import Status

def status_level(modeladmin, request, queryset):
    queryset.update(status='p')
status_level.short_description = "Mark selected stories as published"

class StatusAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    ordering = ['title']
    actions = [status_level]

admin.site.register(Status, StatusAdmin)
