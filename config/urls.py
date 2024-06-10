
from django.contrib import admin
from django.urls import path, include
from config.env import env
urlpatterns = [
    path(f'{env('DJANGO_ADMIN_URL')}/', admin.site.urls),
    path('api/core/', include('apps.core.urls')),
    path('api/location/', include('apps.location.urls')),
]
