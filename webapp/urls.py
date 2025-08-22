from django.urls import path

from webapp.views import ProjectListView, CreateProjectView, DetailProjectView, UpdateProjectView, DeleteProjectView, \
    CreateTaskView, UpdateTaskView, DeleteTaskView, DetailTaskView
from webapp.views.project import hw69

urlpatterns = [
    path('', ProjectListView.as_view(), name='index'),
    path('new/', CreateProjectView.as_view(), name='add_project'),
    path('project/<int:pk>/', DetailProjectView.as_view(), name='detail_project'),
    path('project/<int:pk>/update/', UpdateProjectView.as_view(), name='update_project'),
    path('project/<int:pk>/delete/', DeleteProjectView.as_view(), name='delete_project'),

    path('new/<int:pk>/task/', CreateTaskView.as_view(), name='add_task'),
    path('task/<int:pk>/update/', UpdateTaskView.as_view(), name='update_task'),
    path('task/<int:pk>/delete/', DeleteTaskView.as_view(), name='delete_task'),
    path('task/<int:pk>/detail/', DetailTaskView.as_view(), name='detail_task'),

    path('/hw69/', hw69, name='hw69'),

]
