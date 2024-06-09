from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response

from .models import User
from .permissions import (AnyCanCreatePermission, OwnUpdatePermission)
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated | AnyCanCreatePermission | OwnUpdatePermission]
    queryset = User.objects.all().order_by('-created')
    serializer_class = UserSerializer


class UserAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        password = request.data.get("password")

        if not email or not password:
            return Response(status=400)

        user = User.objects.filter(email=email).first()
        if not email:
            return Response(status=400)

        if not user.check_password(password):
            return Response(status=400)

        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })
