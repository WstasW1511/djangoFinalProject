from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from posts.models import CommentModel
from posts.serializers import CommentsSerializer



class CommentViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, ]
    serializer_class = CommentsSerializer
    queryset = CommentModel.objects.all()
