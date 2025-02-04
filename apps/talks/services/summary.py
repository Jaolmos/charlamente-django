from openai import OpenAI
from django.conf import settings

class GPTSummaryService:
    def __init__(self):
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)
    
    def generate_summary(self, transcript):
        try:
            prompt = """
            Resume este contenido de forma concisa y clara. Debes:

            1. Tema principal
            2. Ideas más importantes (máximo 3)
            3. Conclusión clave

            Mantenlo breve y directo.
            """

            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": prompt
                    },
                    {
                        "role": "user",
                        "content": transcript
                    }
                ],
                max_tokens=300,
                temperature=0.5
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            print(f"Error detallado: {str(e)}")  # Para debug
            raise Exception(f"Error generando resumen: {str(e)}")