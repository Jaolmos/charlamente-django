from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    """
    Modelo de usuario personalizado que extiende de AbstractUser
    """
    class Meta:
        db_table = 'users'  # Nombre de la tabla en la base de datos

