from rest_framework.viewsets import ModelViewSet
from users.serializers.user_serializer import UserSerializer, UserListSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from users.models.user import CustomUser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, ]
    queryset = CustomUser.objects.all()







