from django.contrib import admin
from webapp.models import Task, Type, Statuses, Project


class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'deadline','created_at','updated_at','status', 'project')
    search_fields = ('title',)

class TypeAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'created_at', 'updated_at')

class StatusesAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'created_at', 'updated_at')

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'date_start', 'date_end')



admin.site.register(Task, TaskAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Statuses, StatusesAdmin)
admin.site.register(Project, ProjectAdmin)