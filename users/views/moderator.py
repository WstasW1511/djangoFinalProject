from rest_framework.mixins import *
from django.http import Http404
from posts.models import Posts
from posts.serializers import ModerateSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from rest_framework.validators import ValidationError


class ModeratorViewSet(APIView):
    queryset = Posts.objects.all()
    serializer_class = ModerateSerializer
    permission_classes = [IsAdminUser, ]

    def get(self, request, *args, **kwargs):
        if 'uuid' in kwargs.keys():
            instance = self.queryset.filter(pk=kwargs['uuid']).first()
            serializer = self.serializer_class(instance)
        else:
            instance = self.get_posts()
            serializer = self.serializer_class(instance, many=True)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        if 'uuid' in kwargs.keys():
            try:
                posts = Posts.objects.get(uuid=kwargs['uuid'])
                serializer = self.serializer_class(posts, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(data=serializer.data, status=status.HTTP_204_NO_CONTENT)
            except:
                raise ValidationError()
        return Response(status=status.HTTP_400_BAD_REQUEST)




    def get_posts(self):
        try:
            # instance = Posts.objects.filter(moderate=False)
            instance = Posts.objects.all()
            return instance
        except:
            raise Http404