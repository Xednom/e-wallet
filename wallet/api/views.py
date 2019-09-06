from rest_framework import generics, status, viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import CashSerializer
from wallet.models import Cash


class CashViewSet(viewsets.ModelViewSet):
    serializer_class = CashSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        cash_list = Cash.objects.all()
        qs = cash_list.filter(user__username=self.request.user)
        return qs

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
    

class CashCreateAPIView(generics.CreateAPIView):
    serializer_class = CashSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        cash_list = Cash.objects.all()
        qs = cash_list.filter(user__username = self.request.user)
        return qs

    def perform_create(self, serializer):
        user = self.request.user
        cash_id = self.kwargs.get('id')
        cash = get_object_or_404(Cash, id=cash_id)
        serializer.save(user=user, cash=cash)


class CashRUDAPView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CashSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        cash_list = Cash.objects.all()
        qs = cash_list.filter(user=self.request.user)
        return qs
