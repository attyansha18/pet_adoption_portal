from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

User = get_user_model()

# Signal to log when a new user is created
@receiver(post_save, sender=User)
def user_created(sender, instance, created, **kwargs):
    if created:
        print(f"New user created: {instance.username}")
