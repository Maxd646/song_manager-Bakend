import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SONG_MANAGER_DJANGO_BACKEND.settings')
application = get_wsgi_application()
