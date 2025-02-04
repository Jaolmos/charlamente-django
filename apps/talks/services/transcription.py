import whisper
import os

class WhisperLocalService:
    def __init__(self):
        # Cargar modelo (small es más rápido, pero menos preciso)
        self.model = whisper.load_model("small")
    
    def transcribe(self, file_path):
        try:
            print(f"Iniciando transcripción del archivo: {file_path}")
            print(f"Verificando existencia del archivo: {os.path.exists(file_path)}")
            print(f"Tamaño del archivo: {os.path.getsize(file_path)} bytes")
            # Transcribir
            result = self.model.transcribe(
                file_path,
                language="es",
                fp16=False  # Para CPU
            )
            
            print(f"Transcripción completada. Longitud: {len(result['text'])}")
            return result["text"]
            
        except Exception as e:
            print(f"Error en transcripción: {str(e)}")
            raise Exception(f"Error en transcripción: {str(e)}")