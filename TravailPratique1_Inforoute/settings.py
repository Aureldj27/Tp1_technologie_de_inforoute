import os
from pathlib import Path

# === BASE DIR ===
BASE_DIR = Path(__file__).resolve().parent.parent

# === SÉCURITÉ ===
SECRET_KEY = 'django-insecure-local-dev-key'
DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# === APPLICATIONS ===
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'drf_yasg',
    'graphene_django',
    'django_filters',
    'TP1_Inforoute',
]

# === MIDDLEWARE ===
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# === Templates ===
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'TP1_Inforoute' / 'templates'],  # tes templates custom ici
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

# === URLS & WSGI ===
ROOT_URLCONF = 'TravailPratique1_Inforoute.urls'
WSGI_APPLICATION = 'TravailPratique1_Inforoute.wsgi.application'

# === BASE DE DONNÉES ===
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# === FICHIERS STATIQUES ===
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'TP1_Inforoute' / 'static']  # <-- si tu as un dossier static dans ton app
STATIC_ROOT = BASE_DIR / 'staticfiles'  # <-- collectstatic les mettra ici

# === CONFIGS REST & GRAPHQL ===
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
}

GRAPHENE = {
    'SCHEMA': 'TP1_Inforoute.schema.schema',
}

# === AUTRES ===
LANGUAGE_CODE = 'fr'
TIME_ZONE = 'America/Toronto'
USE_I18N = True
USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'