# from rest_framework.views import APIView
# from rest_framework.permissions import IsAuthenticated
# from posts.models import CommentModel
# from posts.serializers import CommentsSerializer
# from rest_framework.response import Response
# from rest_framework import status
#
#
# class CommentViewSet(APIView):
#     permission_classes = [IsAuthenticated, ]
#     serializer_class = CommentsSerializer
#     queryset = CommentModel.objects.all()
#
#
#     def get(self, request, *args, **kwargs):
#         if 'uuid' in kwargs.keys():
#             comment = CommentModel.objects.get(pk=kwargs['uuid'])
#             serializer = self.serializer_class(comment)
#         else:
#             serializer = self.serializer_class(CommentModel.objects.all(), many=True)
#         return Response(data=serializer.data, status=status.HTTP_200_OK)
#
#
#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data, context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(data=serializer.data, status=status.HTTP_200_OK)
#

from django.http import Http404
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.viewsets import mixins, GenericViewSet
from rest_framework.response import Response
from rest_framework import status
from posts.models import CommentModel
from rest_framework.validators import ValidationError
from posts.permissions import PostCreate

from posts.serializers import CommentsSerializer


class CommentViewSet(mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     mixins.RetrieveModelMixin,
                     GenericViewSet):
    serializer_class = CommentsSerializer
    permission_classes = [AllowAny, ]
    queryset = CommentModel.objects.all()

    def get_permissions(self):
        permission_classes = [AllowAny, ]
        if self.action == 'create':
            permission_classes = [IsAuthenticated]
        elif self.action == 'destroy' or self.action == "update" or self.action == "partial_update":
            permission_classes = [PostCreate, ]
        elif self.action == 'list':
            permission_classes = [AllowAny, ]
        return [permisson() for permisson in permission_classes]

    def get_serializer_class(self):
        serializer_class = CommentsSerializer
        # if self.action == 'create':
        #     serializer_class = CommentCreateSerializer
        # elif self.action == 'update' or self.action == 'partial_update':
        #     serializer_class = CommentUpdateSerializer
        # elif self.action == 'list':
        #     serializer_class = CommentListSerializer
        # elif self.action == 'destroy':
        #     serializer_class = CommentDestroySerializer
        # elif self.action == 'retrieve':
        #     serializer_class = CommentRetrieveSerializer
        return serializer_class

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        queryset = self.queryset.all()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(data={'detail': 'all deleted'}, status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def get_object(self):
        uuid = self.kwargs['pk']
        try:
            instance = self.queryset.get(uuid=uuid)
            return instance
        except:
            raise Http404