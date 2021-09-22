from rest_framework import serializers
from posts.models import CommentModel


class CommentsSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = CommentModel
        fields = (
            "posts",
            "comment",
            'author'
        )
