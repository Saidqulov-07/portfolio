import os
from pathlib import Path

# Loyiha papkasi yo'li
BASE_DIR = Path(__file__).resolve().parent.parent

# Xavfsizlik kaliti (buni hech kimga ko'rsatmang!)
SECRET_KEY = 'yashirin-kalit-yozing'

# Debug rejimi (ishlab chiqish jarayonida True)
DEBUG = True

ALLOWED_HOSTS = ['*'] # Render yoki boshqa serverda ishlash uchun

# Ilovalar ro'yxati
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'aloqa',  # Sizning ilovangiz nomi
    'portfel', # Sizning ikkinchi ilovangiz nomi
]

# Middleware (so'rovlarni boshqarish)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'portfolio_project.urls' # Asosiy URL yo'llari

# Shablonlar (HTML fayllar) sozlamasi
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], # HTML fayllar papkasi
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'portfolio_project.wsgi.application'

# Ma'lumotlar bazasi (standart SQLite)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Til va vaqt
LANGUAGE_CODE = 'uz' # O'zbek tili
TIME_ZONE = 'Asia/Tashkent'

# Statik fayllar (CSS, JS, Rasmlar)
STATIC_URL = 'static/'