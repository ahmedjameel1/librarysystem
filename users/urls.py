from django.urls import path
from django.contrib.auth import logout
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .views import UserCreateAPIView, LoginAPIView, APIKeyView


class CustomLogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({'message': 'Successfully logged out.'}, status=status.HTTP_200_OK)

urlpatterns = [
    path('register/', UserCreateAPIView.as_view(), name='user-register'),
    path('login/', LoginAPIView.as_view(), name='user-login'),
    path('logout/', CustomLogoutView.as_view(), name='user-logout'),
    path('api_key/', APIKeyView.as_view(), name='user-api-key')
]
