from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from users.api.serializers import UserDisplaySerializer

from users.models import CustomUser as user


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserDisplaySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_list = user.objects.filter(username=self.request.user)
        return user_list

class CurrentUserAPIView(APIView):

    def get(self, request):
        serializer = UserDisplaySerializer(request.user)
        return Response(serializer.data)
