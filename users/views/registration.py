from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken, BlacklistMixin
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


from users.models import CustomUser
from users.serializers import UserSerializer, RegistrationSerializer





class RegistrationViewSet(APIView):
    permission_classes = [AllowAny, ]
    serializer_class = RegistrationSerializer
    queryset = CustomUser.objects.all()

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            if serializer.login_user(request, serializer.validated_data['user']):
                response = UserSerializer(serializer.validated_data['user']).data
                response['tokens'] = self.get_tokens_for_user(request.user)
                return Response(data=response, status=status.HTTP_201_CREATED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }