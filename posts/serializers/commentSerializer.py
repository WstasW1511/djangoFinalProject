from rest_framework import serializers
from posts.models import CommentModel


class CommentsSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = CommentModel
        fields = (
            'uuid',
            "posts",
            "comment",
            'author'
        )

    def validate(self, attrs):
        return attrs