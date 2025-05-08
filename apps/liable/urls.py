from django.urls import path
from . import views

app_name = 'apps.liable'
urlpatterns = [
    path('', views.Index.as_view(), name='liable'),
    path('crear/', views.create, name='liable_create'),
    path('detalles/<uuid:pk>', views.Detail.as_view(), name='liable_detail'),
]
