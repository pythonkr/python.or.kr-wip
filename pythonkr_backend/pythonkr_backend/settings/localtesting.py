from pathlib import Path
import os

from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': 'db',
        'NAME': 'pk',
        'USER': 'pk',
        'PASSWD': 'pktesting',
    }
}

#CSRF_TRUSTED_ORIGINS = ["https://pk.iz4u.net"]


# wagtail

STATIC_ROOT = "/app/static"

MEDIA_ROOT = "/app/media"

# bakery

BAKERY_MULTISITE = True
BUILD_DIR = os.path.join("/app/bakery_static", "build")