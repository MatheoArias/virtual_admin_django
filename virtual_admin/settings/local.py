import os
from .base import *

DEBUG = True

ALLOWED_HOSTS = ["*", "db", "localhost", "127.0.0.1"]

# Detectar si se está corriendo en local fuera de Docker
RUN_LOCAL = os.environ.get("RUN_LOCAL") == "1"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME', 'virtual_admin'),
        'USER': os.environ.get('DB_USER', 'postgres'),
        'PASSWORD': os.environ.get('DB_PASSWORD', 'Empl0yee25+'),
        'HOST': os.environ.get('DB_HOST', 'localhost' if RUN_LOCAL else 'db'),
        'PORT': os.environ.get('DB_PORT', '5432'),
    }
}

MEDIA_ROOT = 'media'
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = ["static"] 