import os
from celery import Celery

# Establecer la configuración de Django por defecto para celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'charlamente.settings.local')

# Crear instancia de celery
app = Celery('charlamente')

# Usar la configuración de Django para Celery
app.config_from_object('django.conf:settings', namespace='CELERY')

# Autodescubrir tareas en todas las aplicaciones instaladas
app.autodiscover_tasks() 