from django import forms
from APPJugador.models import Jugador

class FormJugador(forms.ModelForm):
    class Meta:
        model=Jugador
        fields= '__all__'
