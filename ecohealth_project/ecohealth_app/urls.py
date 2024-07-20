from django.urls import path
from . import views

urlpatterns = [
    path('', views.health_data_list, name='health_data_list'),
    path('data/<int:pk>/', views.health_data_detail, name='health_data_detail'),
    path('data/new/', views.health_data_new, name='health_data_new'),
]