import json
import os
import sys

from django.core.exceptions import ImproperlyConfigured


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


secrets = os.getenv('SECRETS', BASE_DIR + '/config/secrets.json')
settings = os.getenv('SETTINGS', BASE_DIR + '/config/settings.json')

with open(secrets) as f:
    secrets = json.loads(f.read())
with open(settings) as f:
    settings = json.loads(f.read())


def get_setting(setting, data=settings):
    try:
        return data[setting]
    except KeyError:
        msg = f'Set the {setting} setting in settings/secrets file'
        raise ImproperlyConfigured(msg)


SECRET_KEY = get_setting('SECRET_KEY', secrets)
DEBUG = get_setting('DEBUG')
ALLOWED_HOSTS = get_setting('ALLOWED_HOSTS')

INSTALLED_APPS = [

    # django applications
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # third part applications
    'isbn_field',
    'languages',

    # internal applications
    'authors',
    'books',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': get_setting('DB_NAME'),
        'USER': get_setting('DB_USER'),
        'PASSWORD': get_setting('DB_PASSWORD', secrets),
        'HOST': get_setting('DB_HOST'),
        'PORT': get_setting('DB_PORT'),
    }
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

ROOT_URLCONF = 'config.urls'
WSGI_APPLICATION = 'config.wsgi.application'

AUTH_PASSWORD_VALIDATORS = []

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = '/static'

MEDIA_URL = '/media/'
MEDIA_ROOT = '/media'

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
    ),
}


if DEBUG:
    from .debug import *

if 'test' in sys.argv:
    from .test import *
