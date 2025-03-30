from django.contrib.auth.models import AbstractUser
from django.db import models


class AppUser(AbstractUser):
    latitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True
    )
    longitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True
    )
    USER_TYPE_CHOICES = [
        ('host', 'Host'),
        ('client', 'Client'),
        ('none', 'None'),  # Default value when no type is selected
    ]
    
    user_type = models.CharField(
        max_length=10, choices=USER_TYPE_CHOICES, default='none'
    )
    
