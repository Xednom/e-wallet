from django.urls import include, path

from rest_framework.routers import DefaultRouter

from users.api.views import CurrentUserAPIView, UserViewSet

from users.api.views import UserViewSet
from wallet.api.views import CashViewSet

router = DefaultRouter()

router.register(r'user', UserViewSet, basename='user')
router.register(r'cash', CashViewSet, basename='Cash')

urlpatterns = [
    path('', include(router.urls)),
]
