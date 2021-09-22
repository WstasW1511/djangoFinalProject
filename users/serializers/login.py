from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.contrib.auth import login
from rest_framework_simplejwt.tokens import RefreshToken
from users.verification import send_sms_code, is_code_correct
from users.models import CustomUser





class LoginSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=12, required=True)
    password = serializers.CharField(max_length=50, required=True)
    class Meta:
        model = CustomUser
        fields = (
            'phone',
            'password',
        )

    def validate(self, attrs):

        if 'phone' and 'password' in attrs.keys():
            user = CustomUser.objects.all().filter(phone=attrs['phone']).first()
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




