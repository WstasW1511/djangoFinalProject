from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from posts.models import Like
from rest_framework.validators import ValidationError


class LikesSerializer(ModelSerializer):
    class Meta:
        model = Like
        fields = (
            '__all__'
        )


class LikeCreateSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Like
        fields = (
            "uuid",
            'post',
            'kind',
            'author'
        )

    def validate(self, attrs):
        request = self.context['request']
        post = attrs['post']

        old_like = Like.objects.filter(author=request.user, post=post).first()
        if old_like:
            if old_like.kind == attrs['kind']:
                raise ValidationError('You check this post yet')
            else:
                # old_like.kind = attrs['kind']
                old_like.delete()
        return attrs
