from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.views.static import serve
from demo.views import base_views

urlpatterns = [
    path('demo/', include('demo.urls')),
    path('common/', include('common.urls')),
    path('board/', include('board.urls')),
    path('admin/', admin.site.urls),
    path('', base_views.index, name='index'), 
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

