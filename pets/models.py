from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Pet(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=50, choices=[('Dog', 'Dog'), ('Cat', 'Cat'), ('Other', 'Other')])
    breed = models.CharField(max_length=100, blank=True, null=True)
    age = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='pet_images/')
    available = models.BooleanField(default=True)
    shelter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shelter_pets')

    def __str__(self):
        return self.name
