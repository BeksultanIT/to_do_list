from django.contrib import admin
from webapp.models import Task, Type, Statuses


class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'deadline','created_at','updated_at','status', 'type')
    search_fields = ('title',)

class TypeAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'created_at', 'updated_at')

class StatusesAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'created_at', 'updated_at')



admin.site.register(Task, TaskAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Statuses, StatusesAdmin)