from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Pet

# Example signal to log when a new pet is saved
@receiver(post_save, sender=Pet)
def pet_saved(sender, instance, created, **kwargs):
    if created:
        print(f"New pet added: {instance.name}")
    else:
        print(f"Pet updated: {instance.name}")
