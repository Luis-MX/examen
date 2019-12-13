from .models import Pelicula
from django.forms import ModelForm,Textarea, TextInput, NumberInput, Select


class PeliculaForm(ModelForm):
    class Meta:
        model = Pelicula
        fields = '__all__'

        widgets = {
            'descripcion': Textarea(attrs={'cols': 6, 'rows': 2,'class':'form-control'}),
            'nombre': TextInput(attrs={'class':'form-control'}),
            'altura': NumberInput(attrs={'class':'form-control'}),
            'periodo': Select(attrs={'class':'form-control'}),
        }

        error_messages = {
            'nombre': {
                'max_length': 50,
                'required': 'Este campo es requerido'
            },
        }
