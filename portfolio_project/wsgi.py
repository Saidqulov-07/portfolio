import os
from django.core.wsgi import get_wsgi_application

# 'portfolio_project.settings' bu sizning settings faylingizning yo'li
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')

application = get_wsgi_application()