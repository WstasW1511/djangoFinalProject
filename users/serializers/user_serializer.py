from rest_framework.serializers import ModelSerializer
from users.models.user import CustomUser
from rest_framework.validators import ValidationError


class UserAdminSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('uuid',
                  'phone',
                  'first_name',
                  'last_name',
                  'is_staff',
                  'is_active',
                  'password',
                  'kind')


class UserListSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            'phone',
            'password',
        )

class UserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            'uuid',
            'first_name',
                  'last_name',)