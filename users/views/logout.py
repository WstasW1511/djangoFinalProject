from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from rest_framework.validators import ValidationError
from users.models import CustomUser
from django.contrib.auth import logout

class LogoutViewSet(APIView):
    permission_classes = [IsAuthenticated, ]


    def post(self, request, *args, **kwargs):
        try:
            user = request.user
            new_refresh = RefreshToken.for_user(user)
            new_refresh.blacklist()
            logout(request)
            return Response({'status': 'true',
                            'detail': 'token is blacklist'}, status=status.HTTP_200_OK)
        except:
           return Response("Bad request")
