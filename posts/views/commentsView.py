from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from posts.models import CommentModel
from posts.serializers import CommentsSerializer
from rest_framework.response import Response
from rest_framework import status


class CommentViewSet(APIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = CommentsSerializer
    queryset = CommentModel.objects.all()


    def get(self, request, *args, **kwargs):
        if 'uuid' in kwargs.keys():
            comment = CommentModel.objects.get(pk=kwargs['uuid'])
            serializer = self.serializer_class(comment)
        else:
            serializer = self.serializer_class(CommentModel.objects.all(), many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_200_OK)

