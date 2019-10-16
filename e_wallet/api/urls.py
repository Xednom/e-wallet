from django.urls import include, path

from rest_framework.routers import DefaultRouter

from users.api.views import CurrentUserAPIView, UserViewSet

from users.api.views import UserViewSet
from wallet.api.views import CashViewSet, WalletViewSet, CashCreateAPIView, CashListAPIView

router = DefaultRouter()

router.register(r'user', UserViewSet, basename='user')
# router.register(r'cash', CashViewSet, basename='cash')
router.register(r'wallet', WalletViewSet, basename='wallet')

urlpatterns = [
    path('', include(router.urls)),
    path('cash-create/', CashCreateAPIView.as_view(), name="cash-create"),
    path('cash-list/', CashListAPIView.as_view(), name="cash-list")
]
