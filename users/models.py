from django.db import models
from django.contrib.auth.models import User
import secrets

class APIKey(models.Model):
    key = models.CharField(max_length=64, unique=True, default=secrets.token_urlsafe)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.key