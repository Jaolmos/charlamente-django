from celery import shared_task
from .models import Talk

@shared_task
def process_talk(talk_id):
    print(f"Iniciando procesamiento de talk_id: {talk_id}")  # Log
    talk = Talk.objects.get(id=talk_id)
    try:
        # Actualizar estado a procesando
        talk.status = 'processing'
        talk.save()

        # Aquí irá la lógica de transcripción cuando decidamos el servicio
        # transcription = transcription_service.transcribe(talk.media_file.path)
        transcription = "Transcripción pendiente de implementar"

        # Guardar resultado
        talk.transcript = transcription
        talk.status = 'completed'
        talk.save()
        # Log

    except Exception as e:
        talk.status = 'failed'
        talk.error_message = str(e)
        talk.save()
        raise