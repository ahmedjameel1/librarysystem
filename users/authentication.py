from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from .models import APIKey

class APIKeyAuthentication(BaseAuthentication):
    """
    Custom authentication class for API key based authentication.
    """

    def authenticate(self, request):
        """
        Performs API key authentication.

        Args:
            request (HttpRequest): The incoming HTTP request.

        Returns:
            tuple: A tuple containing the authenticated user object and None (or raises an AuthenticationFailed exception).
        """
        # Check if the 'HTTP_APIKEY' header is present in the request
        
        key = request.META.get('HTTP_APIKEY')

        if not key:
            raise AuthenticationFailed('APIKey was not provided.')

        try:
            # Retrieve the APIKey object associated with the provided key
            api_key = APIKey.objects.get(key=key)
        except APIKey.DoesNotExist:
            raise AuthenticationFailed('Invalid API Key')

        # Return the authenticated user and None (credentials are not needed)
        return (api_key.user, None)
