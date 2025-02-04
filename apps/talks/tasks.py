from celery import shared_task
from .models import Talk
from .services.transcription import WhisperLocalService
from .services.summary import GPTSummaryService
import logging

logger = logging.getLogger(__name__)

@shared_task
def process_talk(talk_id):
    talk = Talk.objects.get(id=talk_id)
    transcription_service = WhisperLocalService()
    summary_service = GPTSummaryService()
    
    try:
        # Actualizar estado a procesando
        talk.status = 'processing'
        talk.save()
        print("Iniciando procesamiento...")  # Debug log

        # Transcribir con Whisper
        print("Iniciando transcripción...")  # Debug log
        transcription = transcription_service.transcribe(
            talk.media_file.path
        )
        talk.transcript = transcription
        print(f"Transcripción completada. Longitud: {len(transcription)}")  # Debug log

        # Generar resumen con GPT
        print("Iniciando generación de resumen...")  # Debug log
        summary = summary_service.generate_summary(transcription)
        print(f"Resumen generado. Longitud: {len(summary)}")  # Debug log
        talk.summary = summary

        # Actualizar estado a completado
        talk.status = 'completed'
        talk.save()
        print("Proceso completado exitosamente")  # Debug log

    except Exception as e:
        print(f"Error en el proceso: {str(e)}")  # Debug log
        talk.status = 'failed'
        talk.error_message = str(e)
        talk.save()
        raise