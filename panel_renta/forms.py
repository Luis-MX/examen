from .models import Pelicula
from django.forms import ModelForm,Textarea, TextInput, NumberInput, Select


class PeliculaForm(ModelForm):
    class Meta:
        model = Pelicula
        fields = '__all__'
