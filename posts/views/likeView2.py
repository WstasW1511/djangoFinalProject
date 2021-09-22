from rest_framework.mixins import ListModelMixin, DestroyModelMixin, CreateModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated
from posts.models import Like
from posts.serializers import LikesSerializer, LikeCreateSerializer
from rest_framework.validators import ValidationError
from rest_framework.response import Response
from rest_framework import status


class Like2ViewSet(ListModelMixin, DestroyModelMixin, CreateModelMixin, GenericViewSet):
    permission_classes = [IsAuthenticated, ]
    serializer_class = LikesSerializer
    queryset = Like.objects.all()

    def get_serializer_class(self):
        serializer_class = LikesSerializer
        if self.action == 'create':
            serializer_class = LikeCreateSerializer
        return serializer_class

    def list(self, request, *args, **kwargs):
        if 'uuid' in kwargs.keys():
            like = Like.objects.get(pk=kwargs['uuid'])
            serializer = self.serializer_class(like)
        else:
            serializer = self.serializer_class(Like.objects.all(), many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        serializer_data = LikesSerializer(instance).data
        return Response(data=serializer_data, status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        if 'uuid' in kwargs.keys():
            like = Like.objects.filter(pk=kwargs['uuid']).first()
            try:
                like.delete()
            except:
                raise ValidationError("cound not find object by uuid")
        else:
            raise ValidationError('not sent id')
        return Response(data={"details": "object deleted!"}, status=status.HTTP_200_OK)
