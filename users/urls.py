from users.views import RegistrationViewSet, LogoutViewSet, UserViewSet, LoginViewSet
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from users.views import ModeratorViewSet
router = DefaultRouter()

router.register('users/', UserViewSet)




urlpatterns = [
    path('registration/', RegistrationViewSet.as_view()),
    path('mod/', ModeratorViewSet.as_view()),
    re_path(r'^mod/(?P<uuid>[0-9a-f]{8}\-[0-9a-f]{4}\-4[0-9a-f]{3}\-[89ab][0-9a-f]{3}\-[0-9a-f]{12})/$',
            ModeratorViewSet.as_view()),
    path('login/', LoginViewSet.as_view()),
    path('logout/', LogoutViewSet.as_view()),

] + router.urls
