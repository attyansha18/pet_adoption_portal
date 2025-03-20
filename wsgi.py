import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pet_adoption.settings')

application = get_wsgi_application()

# Adding Whitenoise for serving static files
application = WhiteNoise(application, root='/path/to/static/files')
