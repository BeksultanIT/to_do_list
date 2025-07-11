from _pyrepl.commands import delete

from django.urls import path

from webapp.views import IndexView, CreateTaskView, DetailView, UpdateView, DeleteView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('new/', CreateTaskView.as_view(), name='add_task'),
    path('task/<int:pk>/', DetailView.as_view(), name='detail_task'),
    path('task/<int:pk>/update/', UpdateView.as_view(), name='update_task'),
    path('task/<int:pk>/delete', DeleteView.as_view(), name='delete_task'),
]
