import os

from environs import Env
from pathlib import Path


env = Env()
env.read_env()


ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', '127.0.0.1')

SECRET_KEY = env.str('SECRET_KEY', '$ecretK34')

DEBUG = env.bool('DEBUG', True)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': env('DATABASE_NAME'),
    }
}

INSTALLED_APPS = ['datacenter']

ROOT_URLCONF = 'project.urls'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]

USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True
