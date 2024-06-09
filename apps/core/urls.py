from django.urls import (path, include)
from rest_framework import routers

from .views import (UserViewSet, UserAuthToken)

app_name = 'user'

router = routers.DefaultRouter()
router.register('users', UserViewSet, basename='User')

urlpatterns = [
    path('auth-token/', UserAuthToken.as_view(), name='token_auth'),
    path('', include(router.urls)),

]
