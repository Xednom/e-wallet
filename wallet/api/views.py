from rest_framework import generics, status, viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import CashSerializer, WalletSerializer
from wallet.models import Cash, Wallet


class CashViewSet(viewsets.ModelViewSet):
    serializer_class = CashSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        cash_list = Cash.objects.all()
        qs = cash_list.filter(user=self.request.user)
        return qs

    def perform_create(self, serializer):
        user = self.request.user
        return serializer.save(user=user)


class WalletViewSet(viewsets.ModelViewSet):
    serializer_class = WalletSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        wallet_list = Wallet.objects.all()
        qs = wallet_list.filter(user__username=self.request.user)
        return qs
    
    def perform_create(self, serializer):
        if Wallet.objects.filter(user__username=self.request.user).exists():
            raise ValidationError("User with this ID already exists.")
        return serializer.save(user=self.request.user)


class CashCreateAPIView(generics.CreateAPIView):
    queryset = Cash.objects.all()
    serializer_class = CashSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user, wallet_user=user)

class CashRUDAPView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CashSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        cash_list = Cash.objects.all()
        qs = cash_list.filter(user=self.request.user)
        return qs


class CashListAPIView(generics.ListAPIView):
    serializer_class = CashSerializer
    permision_classes = [IsAuthenticated]

    def get_queryset(self):
        cash_list = Cash.objects.all()
        user = self.request.user
        return cash_list.filter(user__username=user)
