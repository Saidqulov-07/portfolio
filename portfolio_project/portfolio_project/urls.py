from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

# Barcha viewlarni shu yerda import qilamiz
from contact.views import contact_view
from portfolio.views import index # portfolio ilovasidagi index ni chaqiramiz

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),  # Bosh sahifa
    path('api/contact/', contact_view),
]

# Media fayllar (rasmlar) ishlashi uchun kerakli qator
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)