import os
from django.core.wsgi import get_wsgi_application

# 'settings' - chunki faylingiz root'da turibdi
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

application = get_wsgi_application()