from django.contrib import admin
from .models import Comment


class CommenAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'url', 'text', 'created_time']


admin.site.register(Comment, CommenAdmin)
