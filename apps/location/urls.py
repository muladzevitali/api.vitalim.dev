from django.urls import (path, include)
from rest_framework import routers

from .views import (LocationViewSet, LocationDistanceViewSet)

app_name = 'locations'

router = routers.DefaultRouter()
router.register('locations', LocationViewSet, basename='Location')
router.register('distances', LocationDistanceViewSet, basename='LocationDistances')

urlpatterns = [
    path('', include(router.urls)),
]
