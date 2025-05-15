from django.contrib import admin
from django.urls import path,include
from .views import IndexView
from django.conf.urls.static import static
from .settings.local import MEDIA_ROOT, MEDIA_URL


urlpatterns = [
    path('admin/', admin.site.urls),
    path("unicorn/", include("django_unicorn.urls")),
    path('', IndexView.as_view(), name='index'),
    path('personal/',include('apps.liable.urls',namespace='liable') ),
    
]+ static(MEDIA_URL, document_root=MEDIA_ROOT)
