from django.contrib import admin
from .models import Task
from django.contrib.auth.models import User
# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display=('task','is_completed','updated_at')
    search_fields = ('task',)
admin.site.register(Task,TaskAdmin)


