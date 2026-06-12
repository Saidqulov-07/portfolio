import os
from django.core.wsgi import get_wsgi_application

# 'sozlamalar' bu sizning settings faylingiz nomi
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.sozlamalar')

application = get_wsgi_application()