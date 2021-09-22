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


    # def validate(self, attrs):
    #
    #     if 'phone' and 'password' in attrs.keys():
    #
    #         attrs['user'] = user
    #         # if not user:
    #         #     user = CustomUser.objects.create_user(attrs['phone'])
    #         #     attrs['user'] = user
    #     else:
    #         raise ValidationError('try again')
    #
    #     return attrs
    #
    # def login_user(self, request, user):
    #     if self.validated_data['user']:
    #         login(request, user)
    #         return True
    #     else:
    #         return False
    #
    #
    #
    # phone = serializers.CharField(max_length=12, required=True)
    # otp = serializers.CharField(max_length=4, required=False)
    # refresh = serializers.CharField(max_length=100, required=False)
    #
    # class Meta:
    #     fields = (
    #         'phone',
    #         'otp',
    #         'refresh',
    #     )
    #
    # def validate(self, attrs):
    #     attrs['otp_check'] = False
    #     if 'phone' in attrs.keys():
    #         user = CustomUser.objects.filter(phone=attrs['phone']).first()
    #         if not user:
    #
    #             user = CustomUser.objects.create_user(attrs['phone'])
    #             attrs['user'] = user
    #         else:
    #             attrs['user'] = user
    #     else:
    #         raise ValidationError('"phone" fields not found, try again')
    #
    #     if 'otp' in attrs.keys():
    #         check = is_code_correct(attrs['phone'], attrs['otp'])
    #         if check:
    #             attrs['otp_check'] = check
    #         else:
    #             raise ValidationError('OTP incorrect or OTP lifetime pass')
    #     else:
    #         sms = send_sms_code(attrs['phone'], 'Verify code: ')
    #         attrs['sms'] = sms
    #     return attrs
    #
    # def login_user(self, request, user):
    #     if self.validated_data['otp_check']:
    #         login(request, user)
    #         return True
    #     else:
    #         return False
    #
    # def check_token(self, token):
    #     pass



