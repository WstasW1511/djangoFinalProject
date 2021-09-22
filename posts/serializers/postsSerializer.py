from rest_framework import serializers

from posts.models import Posts
from .commentSerializer import CommentsSerializer
from .like_serializer import LikesSerializer


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = (
            'uuid',
            'author',
            'text',
            'view'

        )
        read_only_fields = ('created_at', 'update_at')


class PostListSerializer(serializers.ModelSerializer):
    comment = CommentsSerializer(required=False, many=True)
    likes = LikesSerializer(required=False, many=True)

    class Meta:
        model = Posts
        fields = (
            'uuid',
            'author',
            'text',
            'view',
            'comment',
            'likes',
        )
        read_only_fields = ('created_at', 'update_at')


class PostCreateSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Posts
        fields = (
            'text',
            'author',
            'view'
        )

    def create(self, validated_data):
        instance = super().create(validated_data)
        instance.moderate = False
        instance.save()
        return instance


class PostUpdateSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Posts
        fields = (
            'uuid',
            'author',
            'text',
            'view'

        )
        read_only_fields = ('created_at', 'update_at')


class ModerateSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Posts
        fields = (
            'uuid',
            'author',
            'moderate',
            'view'
        )

    def validate(self, attrs):
        text = attrs.pop('text', None)
        return attrs
