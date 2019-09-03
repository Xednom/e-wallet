from django.urls import path
from users.viewsets import CurrentUserAPIView

app_name='users'
urlpatterns = [
    path('users/', CurrentUserAPIView.as_view(), name='current-user')
]
