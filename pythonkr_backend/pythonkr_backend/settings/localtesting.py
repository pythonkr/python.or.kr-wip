import os

import logfire

from .base import *

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": "db",
        "NAME": "pk",
        "USER": "pk",
        "PASSWORD": "pktesting",
    }
}

# CSRF_TRUSTED_ORIGINS = ["https://pk.iz4u.net"]


# wagtail

STATIC_ROOT = "/app/static"

MEDIA_ROOT = "/app/media"

# bakery

BAKERY_MULTISITE = True
BUILD_DIR = os.path.join("/app/bakery_static", "build")


# check WSGI environment
IS_PRODUCTION_SERVER = os.environ.get("IS_WSGI_ENVIRONMENT", "False") == "True"


# logfire settings
if IS_PRODUCTION_SERVER:
    logfire.configure(environment="localtest")
    logfire.instrument_django()

# testing
CELERY_ALWAYS_EAGER = True
