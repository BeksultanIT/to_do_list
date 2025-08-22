from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add, name='api_add'),
    path('subtract/', views.subtract, name='api_subtract'),
    path('multiply/', views.multiply, name='api_multiply'),
    path('divide/', views.divide, name='api_divide'),
]
