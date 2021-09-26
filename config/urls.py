from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from demo.views import base_views

urlpatterns = [
    path('demo/', include('demo.urls')),
    path('common/', include('common.urls')),
    # path('board/', include('board.urls')),
    path('admin/', admin.site.urls),
    path('', base_views.index, name='index'), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
