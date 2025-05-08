from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='liable'),
    path('crear/', views.create, name='liable_create'),
]
