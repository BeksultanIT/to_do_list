from _pyrepl.commands import delete

from django.urls import path

from webapp.views import index, new, detail_article, update_task, delete_task

urlpatterns = [
    path('', index, name='index'),
    path('new/', new, name='add_task'),
    path('task/<int:pk>/', detail_article, name='detail_task'),
    path('task/<int:pk>/update/', update_task, name='update_task'),
    path('task/<int:pk>/delete', delete_task, name='delete_task'),
]
