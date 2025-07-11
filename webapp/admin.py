from django.contrib import admin
from webapp.models import Task


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'deadline',)
    search_fields = ('title',)


admin.site.register(Task, ArticleAdmin)