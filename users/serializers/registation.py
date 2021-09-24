from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.contrib.auth import login
from users.models import CustomUser
from utils.const import GenModeratorChoice




class RegistrationSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=12, required=True)
    # first_name = serializers.CharField(max_length=50, )
    # last_name = serializers.CharField(max_length=50, )
    password = serializers.CharField(max_length=50, required=True)
    # refresh = serializers.CharField(max_length=500, required=False)
    kind = serializers.ChoiceField(choices=GenModeratorChoice)
    # is_staff = serializers.BooleanField(default=True)
    # is_active = serializers.BooleanField(default=True)
    class Meta:
        model = CustomUser
        fields = (
            'phone',
            # 'first_name',
            # 'last_name',
            'password',
            # 'refresh'
            'kind',
            # 'is_staff',
            # 'is_active'
        )
    def validate(self, attrs):

        if 'phone' and 'password' in attrs.keys():
            user = CustomUser.objects.create_user(phone=attrs['phone'],
                                                  # first_name=attrs['first_name'],
                                                  # last_name=attrs['last_name'],
                                                  password=attrs['password'])
            attrs['user'] = user
        else:
            raise ValidationError('try again')

        return attrs

    def login_user(self, request, user):
        if self.validated_data['user']:
            login(request, user)
            return True
        else:
            return False