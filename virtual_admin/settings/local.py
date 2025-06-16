from dotenv import load_dotenv
import os
from .base import *

# Charge environment variables from .env file
load_dotenv()

DEBUG = True

#All hosts are allowed in development
ALLOWED_HOSTS = ["*", "db", "localhost", "127.0.0.1"]

#If running locally, set RUN_LOCAL to True
RUN_LOCAL = os.environ.get("RUN_LOCAL") == "1"

#Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('localhost' if RUN_LOCAL else 'db'),
        'PORT': os.environ.get('DB_PORT'),
    }
}

#Root directory for media files in production
MEDIA_ROOT = 'media'

#Root directory for charge the style files in production
STATIC_ROOT = BASE_DIR / "staticfiles"

#Directories added to the search path for static files
STATICFILES_DIRS = ["static"] 