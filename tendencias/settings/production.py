from .base import *


DEBUG = True

ALLOWED_HOSTS = []



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME':  'd7nkq45plitpmr',
        'USER': 'plhmihwhasgpsr',
        'PASSWORD': 'bb3e7ff5e40e784fe5cde263171652a64493cf64d72f1c5faf33af224d8f194f',
        'HOST': 'ec2-52-7-39-178.compute-1.amazonaws.com',
        'PORT': '5432',


    }
}


STATICFILES_DIRS = (BASE_DIR, 'static')