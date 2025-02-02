from django import forms
from .models import Talk

class TalkForm(forms.ModelForm):
    class Meta:
        model = Talk
        fields = ['title', 'speaker', 'media_file']
        
    def clean_media_file(self):
        file = self.cleaned_data.get('media_file')
        if file:
            # Se obtiene la extensión del archivo
            ext = file.name.split('.')[-1].lower()
            # Se definen los tipos permitidos
            allowed_types = ['mp3', 'wav', 'mp4', 'avi', 'mov']
            
            if ext not in allowed_types:
                raise forms.ValidationError(
                    'Tipo de archivo no permitido. Use: mp3, wav, mp4, avi, mov'
                )
        return file