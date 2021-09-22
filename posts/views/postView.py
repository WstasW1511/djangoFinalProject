from rest_framework.mixins import ListModelMixin, RetrieveModelMixin,DestroyModelMixin,CreateModelMixin, \
    UpdateModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated
from posts.serializers import *
from users.permissions import PostCreate
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from posts.filters import *

class PostViewSet(ListModelMixin,
                  RetrieveModelMixin,
                  UpdateModelMixin,
                  DestroyModelMixin,
                  CreateModelMixin,
                  GenericViewSet):

    queryset = Posts.objects.all()
    serializer_class = PostSerializer

    filter_backends = (filters.DjangoFilterBackend, )
    filterset_class = PostsFilterSet

    def get_permissions(self):
        permissions_classes = [AllowAny, ]
        if self.action == 'create':
            permissions_classes = [IsAuthenticated, PostCreate ]
        if self.action == 'retrieve':
            permissions_classes = [IsAuthenticated, ]
        if self.action == 'update' or self.action == 'destroy' or self.action == 'partial_update':
            permissions_classes = [IsAuthenticated, PostCreate]
        return [permission() for permission in permissions_classes]

    def get_serializer_class(self):
        serializer_class = PostSerializer
        if self.action == 'create':
            serializer_class = PostCreateSerializer
        elif self.action == 'list':
            serializer_class = PostListSerializer
        elif self.action == 'update':
            serializer_class = PostUpdateSerializer
        return serializer_class


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        serializer_data = PostSerializer(instance).data
        return Response(data=serializer_data, status=status.HTTP_201_CREATED)


    def list(self, request, *args, **kwargs):
        #instance = self.get_posts()
        filtered_queryset = self.filter_queryset(self.queryset.all())
        serializer = self.get_serializer(filtered_queryset, many=True)
        #serializer = self.get_serializer(instance, many=True)
        return Response(serializer.data)


    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def get_posts(self):
        author = self.request.user
        try:
            instance = Posts.objects.all()
            return instance
        except:
            raise Http404