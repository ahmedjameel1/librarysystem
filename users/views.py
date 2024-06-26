from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import login
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer, LoginSerializer
from .models import APIKey

class UserCreateAPIView(generics.CreateAPIView):
    """
    API endpoint for user registration.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

class LoginAPIView(APIView):
    """
    API endpoint for user login.
    """
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
    

class APIKeyView(APIView):
    """
    API endpoint for getting the API KEY.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        if not user.is_anonymous:
            try:
                api_key = APIKey.objects.get(user=user).key
                return Response({"api_key": api_key}, status=status.HTTP_200_OK)
            except APIKey.DoesNotExist:
                return Response({"error": "API key does not exist for this user."},
                                status=status.HTTP_404_NOT_FOUND)
        return Response({"error": "authentication is required."},
                        status=status.HTTP_401_UNAUTHORIZED)
