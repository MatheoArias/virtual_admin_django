from django.urls import path
from . import views

app_name = 'apps.liable'
urlpatterns = [
    path('', views.LiableIndexView.as_view(), name='liable-index'),
    path('create/', views.LiableCreateView.as_view(), name='liable-create'),
]
