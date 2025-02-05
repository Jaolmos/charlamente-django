from django import forms
from .models import Talk

class TalkForm(forms.ModelForm):
    class Meta:
        model = Talk
        fields = ['title', 'speaker', 'media_file']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'width: 500px; min-width: 500px; color: #ffffff; background-color: #2d2d30;',
                'placeholder': 'Ingresa el título de la charla'
            }),
            'speaker': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'width: 500px; min-width: 500px; color: #ffffff; background-color: #2d2d30;',
                'placeholder': 'Nombre del presentador'
            })
        }
        
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