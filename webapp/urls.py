from django.urls import path

from webapp.views import index, new, detail_article

urlpatterns = [
    path('', index, name='index'),
    path('new/', new, name='new'),
    path('article/<int:pk>/', detail_article, name='detail_article'),
]