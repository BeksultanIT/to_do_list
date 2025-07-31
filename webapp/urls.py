from django.urls import path

from webapp.views import TaskListView, CreateTaskView, DetailTaskView, UpdateTaskView, DeleteTaskView

urlpatterns = [
    path('', TaskListView.as_view(), name='index'),
    path('new/', CreateTaskView.as_view(), name='add_project'),
    path('project/<int:pk>/', DetailTaskView.as_view(), name='detail_project'),
    path('project/<int:pk>/update/', UpdateTaskView.as_view(), name='update_project'),
    path('project/<int:pk>/delete', DeleteTaskView.as_view(), name='delete_project'),
]
