from django.urls import path

from webapp.views import ProjectListView, CreateProjectView, DetailProjectView, UpdateProjectView, DeleteProjectView, \
    CreateTaskView

urlpatterns = [
    path('', ProjectListView.as_view(), name='index'),
    path('new/', CreateProjectView.as_view(), name='add_project'),
    path('project/<int:pk>/', DetailProjectView.as_view(), name='detail_project'),
    path('project/<int:pk>/update/', UpdateProjectView.as_view(), name='update_project'),
    path('project/<int:pk>/delete/', DeleteProjectView.as_view(), name='delete_project'),

    path('new/<int:pk>/', CreateTaskView.as_view(), name='add_task'),

]
