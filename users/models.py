from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_shelter = models.BooleanField(default=False)
    is_adopter = models.BooleanField(default=True)
