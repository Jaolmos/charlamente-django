import os
from .base import *  # noqa

# Variable de entorno para determinar el ambiente de ejecución
DJANGO_ENV = os.getenv('DJANGO_ENV', 'development')

# Cargamos las configuraciones según el ambiente
if DJANGO_ENV == 'production':
    from .production import *  
else:
    from .local import *  