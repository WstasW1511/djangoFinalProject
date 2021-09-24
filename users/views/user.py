from users.serializers.user_serializer import UserSerializer, UserListSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, DestroyModelMixin, RetrieveModelMixin, UpdateModelMixin
from users.permissions import UserCreate
from users.models import CustomUser


class UserViewSet(ListModelMixin, DestroyModelMixin,RetrieveModelMixin,UpdateModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, ]
    queryset = CustomUser.objects.all()


    def get_permissions(self):
        permissions_classes = [IsAuthenticated, ]
        if self.action == 'retrieve':
            permissions_classes = [IsAdminUser, UserCreate]
        if self.action == 'update' or self.action == 'destroy' or self.action == 'partial_update':
            permissions_classes = [IsAdminUser, UserCreate]
        return [permission() for permission in permissions_classes]

    def get_serializer_class(self):
        serializer_class = UserSerializer
        if self.action == 'list':
            serializer_class = UserListSerializer
        elif self.action == 'retrieve':
            serializer_class = UserSerializer
        return serializer_class

    def list(self, request, *args, **kwargs):
        user = CustomUser.objects.all()
        serializer = self.serializer_class(user, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)
