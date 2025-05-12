import os
from .base import *

DEBUG = True

ALLOWED_HOSTS = ["*","db","localhost", "127.0.0.1"]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME', 'virtual_admin'),
        'USER': os.environ.get('DB_USER', 'postgres'),
        'PASSWORD': os.environ.get('DB_PASSWORD', '123'),
        'HOST': os.environ.get('DB_HOST', 'db'),
        'PORT': os.environ.get('DB_PORT', '5432'),
    }
}

STATICFILES_DIRS = ['static']

MEDIA_ROOT = BASE_DIR.parent/'media'
