from django.urls import path

from webapp.views import index, new

urlpatterns = [
    path('', index),
    path('new/', new),

]