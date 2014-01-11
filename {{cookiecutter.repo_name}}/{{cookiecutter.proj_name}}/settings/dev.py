from .base import *
from os.path import abspath, basename, dirname, join, normpath
from sys import path

# DJANGO_ROOT is where the manage.py file is
DJANGO_ROOT = dirname(dirname(abspath(__file__)))


# Setup a sqlite database for local deployment

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': join(DJANGO_ROOT, 'mydb.sqlite3'),
    }
}

STATIC_ROOT = ''

STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    normpath(join(DJANGO_ROOT, 'static')),
)