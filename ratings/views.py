from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from .permissions import IsOwner
from users.authentication import APIKeyAuthentication
from .models import Rating
from .serializers import RatingSerializer

class RatingListCreate(generics.ListCreateAPIView):
    """
    API endpoint for listing and creating ratings.
    """
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, APIKeyAuthentication]

class RatingRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint for retrieving, updating and deleting a rating instance.
    """
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    authentication_classes = [SessionAuthentication, APIKeyAuthentication]
