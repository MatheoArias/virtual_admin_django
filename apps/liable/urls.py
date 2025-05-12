from django.urls import path
from . import views

app_name = 'apps.liable'
urlpatterns = [
    path('', views.IndexView.as_view(), name='liable'),
]
