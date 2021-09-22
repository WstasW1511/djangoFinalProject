from django.http import HttpResponse
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken, BlacklistMixin
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from django.contrib.auth import login, logout

from users.models import CustomUser
from users.serializers import LoginSerializer, UserSerializer

class LoginViewSet(APIView):
    permission_classes = [AllowAny, ]
    serializer_class = LoginSerializer
    queryset = CustomUser.objects.all()

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            if serializer.login_user(request, serializer.validated_data['user']):
                response = UserSerializer(serializer.validated_data['user']).data
                response['tokens'] = self.get_tokens_for_user(request.user)

                return Response(data=response, status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }


    #
    # def post(self, request, *args, **kwargs):
    #     serializer = self.serializer_class(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     if serializer.login_user(request, serializer.validated_data['user']):
    #         response = UserSerializer(serializer.validated_data['user']).data
    #         response['tokens'] = self.get_tokens_for_user(request.user)
    #         return Response(data=response, status=status.HTTP_200_OK)
    #     else:
    #         return Response(data={'details': 'OTP send', 'sms': serializer.validated_data['sms']}, status=status.HTTP_200_OK)
    #
    # def get_tokens_for_user(self, user):
    #     refresh = RefreshToken.for_user(user)
    #     return {
    #         'refresh': str(refresh),
    #         'access': str(refresh.access_token),
    #     }
