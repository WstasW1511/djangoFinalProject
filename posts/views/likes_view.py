from rest_framework.viewsets import ModelViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, DestroyModelMixin, CreateModelMixin
from rest_framework.viewsets import GenericViewSet
from posts.models import Like
from posts.serializers import LikesSerializer, LikeCreateSerializer
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from posts.permissions import LikeReadOrCreate
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


class LikesViewSet(ListModelMixin, RetrieveModelMixin, DestroyModelMixin, CreateModelMixin, GenericViewSet):
    serializer_class = LikesSerializer
    queryset = Like.objects.all()

    def get_permissions(self):
        permissions_classes = [AllowAny, ]
        if self.action == 'retrieve' or self.action == 'post':
            permissions_classes = [IsAuthenticated, LikeReadOrCreate]
        if self.action == 'update' or self.action == 'destroy' or self.action == 'partial_update':
            permissions_classes = [IsAuthenticated, LikeReadOrCreate]
        return [permission() for permission in permissions_classes]

    def get_serializer_class(self):
        serializer_class = LikesSerializer
        if self.action == 'post':
            serializer_class = LikeCreateSerializer
        return serializer_class

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        serializer_data = LikesSerializer(instance).data
        return Response(data=serializer_data, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        instance = self.get_like()
        serializer = self.get_serializer(instance, many=True)
        return Response(serializer.data)

    def get_like(self):
        try:
            instance = Like.objects.all()
            return instance
        except:
            raise Http404
