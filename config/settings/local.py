"""Development settings."""

from .base import *
from .base import env

SECRET_KEY = env('DJANGO_SECRET_KEY')

DEBUG = True

ALLOWED_HOSTS = ['0.0.0.0', 'localhost']

# django-extensions
INSTALLED_APPS += ['django_extensions']
