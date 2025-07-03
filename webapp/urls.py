from django.urls import path

from webapp.views import index, new, detail_article, update_task

urlpatterns = [
    path('', index, name='index'),
    path('new/', new, name='add_task'),
    path('task/<int:pk>/', detail_article, name='detail_task'),
    path('update/<int:pk>/update/', update_task, name='update_task'),
]
