from datetime import timedelta

import dj_database_url
import redis
import requests_cache

from .base import *


BASE_NAME = BASE_DOMAIN = 'localhost'
BASE_URL = f"http://{BASE_DOMAIN}:8000"

###############################################################################
# Core

DEBUG = True
SECRET_KEY = 'dev'

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '.ngrok.io']

INSTALLED_APPS += ['django_extensions', 'livereload', 'debug_toolbar']

MIDDLEWARE += ['livereload.middleware.LiveReloadScript']
MIDDLEWARE.insert(0, 'debug_toolbar.middleware.DebugToolbarMiddleware')

###############################################################################
# Databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'elections_dev',
        'HOST': '127.0.0.1',
    },
    'remote': dj_database_url.config(),
}

###############################################################################
# Caches

connection = redis.from_url(os.environ['REDIS_URL'])
requests_cache.install_cache(
    backend='redis',
    backend_options=dict(connection=connection),
    expire_after=timedelta(minutes=5),
)

###############################################################################
# Django Debug Toolbar

INTERNAL_IPS = ['127.0.0.1']

DEBUG_TOOLBAR_CONFIG = {'SHOW_COLLAPSED': True}
