from django.urls import path
from .views import base_views, demo_views

app_name = 'demo'

urlpatterns = [
    path('', base_views.index, name='index'),
    path('<int:demo_id>/', base_views.detail, name='detail'),
    path('create/', demo_views.demo_create, name='demo_create'),
]
