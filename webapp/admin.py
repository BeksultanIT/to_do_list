from django.contrib import admin
from webapp.models import Task


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status', 'deadline',)
    search_fields = ('title',)
admin.site.register(Task, ArticleAdmin)