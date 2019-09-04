from django.urls import include, path

from rest_framework.routers import DefaultRouter

from wallet.api import views as cv

from .views import CashViewSet

router = DefaultRouter()

router.register(r'cash', cv.CashViewSet, basename='Cash')

urlpatterns = [
    path('', include(router.urls))
]
