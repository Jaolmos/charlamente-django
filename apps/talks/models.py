from django.db import models
from django.conf import settings
from apps.users.models import CustomUser

# Create your models here.

class Talk(models.Model):
    """
    Modelo para almacenar charlas (audio/video) y sus transcripciones/resúmenes
    """
    user = models.ForeignKey(
        CustomUser, 
        on_delete=models.CASCADE,
        related_name='talks'
    )
    title = models.CharField(max_length=255)
    speaker = models.CharField(max_length=255)
    
    media_file = models.FileField(
        upload_to='talks/',
        help_text='Puedes subir archivos de audio o video'
    )
    
    transcript = models.TextField(blank=True)
    summary = models.TextField(blank=True)
    share_token = models.CharField(max_length=100, unique=True, blank=True)
    
    STATUS_CHOICES = [
        ('pending', 'Pendiente'),
        ('processing', 'Procesando'),
        ('completed', 'Completado'),
        ('error', 'Error'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'talks'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} - {self.speaker}"