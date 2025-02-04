from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Local apps    
    'apps.core',
    'apps.users',
    'apps.talks',
    #third_party_apps
    'django_celery_results'
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

ROOT_URLCONF = 'charlamente.urls'

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

WSGI_APPLICATION = 'charlamente.wsgi.application'

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]


# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'users.CustomUser'


# Auth settings
LOGIN_URL = 'login'
LOGOUT_REDIRECT_URL = 'home'
LOGIN_REDIRECT_URL = 'talk_list'
    

# Configuración de Celery
CELERY_BROKER_URL = 'amqp://localhost'  # Conexión con RabbitMQ
CELERY_RESULT_BACKEND = 'django-db'     # Almacena resultados en la BD
CELERY_ACCEPT_CONTENT = ['json']        # Formato de mensajes
CELERY_TASK_SERIALIZER = 'json'         # Serialización de tareas
CELERY_RESULT_SERIALIZER = 'json'       # Serialización de resultados
CELERY_TIMEZONE = TIME_ZONE            # Zona horaria

# Configuración de OpenAI
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
