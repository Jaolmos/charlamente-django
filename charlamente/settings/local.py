from .base import *
from pathlib import Path
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Ruta al archivo .env (asegurarnos que encuentra el archivo)
env_path = BASE_DIR / '.env'
load_dotenv(env_path)


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
DATABASES = {
    'default': {
        'ENGINE': os.getenv('DB_ENGINE'),
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
        'OPTIONS': {
            'charset': 'utf8mb4'
        }
    }
}