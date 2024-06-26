from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from .models import APIKey

@receiver(user_logged_in)
def create_api_key(sender, user, request, **kwargs):
    if not APIKey.objects.filter(user=user).exists():
        APIKey.objects.create(user=user)
