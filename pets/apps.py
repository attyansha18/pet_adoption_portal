from django.apps import AppConfig

class PetsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pets'

    def ready(self):
        import pets.signals  # Import signals here
