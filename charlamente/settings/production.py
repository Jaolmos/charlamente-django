from .base import *  # noqa

DEBUG = False

# TODO: Configure production settings
SECRET_KEY = None  # Should be set in environment variables
ALLOWED_HOSTS = []  # Configure allowed hosts

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'charlamente_db',
        # Add other database settings
    }
}