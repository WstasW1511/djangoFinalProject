from django.urls import re_path, path
from rest_framework.routers import DefaultRouter
from posts.views import PostViewSet, CommentViewSet, Like2ViewSet, AnaliticViewSet


router = DefaultRouter()
router.register('list', PostViewSet)
router.register('comment', CommentViewSet)


urlpatterns = [
    re_path(r'^likes/(?P<uuid>[0-9a-f]{8}\-[0-9a-f]{4}\-4[0-9a-f]{3}\-[89ab][0-9a-f]{3}\-[0-9a-f]{12})/$',
                    Like2ViewSet.as_view({'get': 'destroy'})),
    path('likes/', Like2ViewSet.as_view({'get': 'list'})),
    path('likes/create/', Like2ViewSet.as_view({'post': 'create'})),
    path('analitic/', AnaliticViewSet.as_view()),



] + router.urls
