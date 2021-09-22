from rest_framework.serializers import ModelSerializer
from users.models.user import CustomUser
from rest_framework.validators import ValidationError


class UserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('__all__')


class UserListSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            'phone',
            'password',
        )