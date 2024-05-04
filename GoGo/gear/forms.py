from django import forms
from django.contrib.auth.models import User
from .models import Avatar, Vuelo

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class VueloSearchForm(forms.Form):
    nombre = forms.CharField(
        max_length=50, required=True, label="Ingresar nombre del vuelo"
    )
    disponible = forms.BooleanField(required=False, label="Sólo vuelos disponibles")
    capacidad_minima = forms.IntegerField(required=False, label="Vuelos con capacidad mayor a:")
    tipo_de_vuelo = forms.ChoiceField(choices=Vuelo.Tipo.choices)


class AvatarCreateForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['image']