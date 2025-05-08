from django import forms
from django.forms import ModelForm
from .models import Liable
from apps.position.models import Position


class LiableForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['position'].empty_label = "Seleccione un cargo"

    class Meta:
        model = Liable
        fields = [
            'name',
            'lastName',
            'position',
            'email',
            'telephone',
            'workstation',
            'image',
            'active']

        labels = {
            'name': 'Nombres',
            'lastName': 'Apellidos',
            'email': 'Correo Electrónico',
            'telephone': 'Teléfono',
            'workstation': 'Puesto de trabajo',
            'position': 'Cargo',
            'image': '¡Cargue su fotografía!',
            'active': 'Estado',
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form__input',
                    'placeholder': 'Ingrese sus nombres'
                }
            ),
            'lastName': forms.TextInput(
                attrs={
                    'class': 'form__input',
                    'placeholder': 'Ingrese sus Apellidos'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form__input',
                    'placeholder': 'Ingrese su correo electrónico'
                }
            ),
            'telephone': forms.TextInput(
                attrs={
                    'class': 'form__input',
                    'placeholder': 'Ingrese su teléfono'
                }
            ),
            'workstation': forms.TextInput(
                attrs={
                    'class': 'form__input',
                    'placeholder': '¿Cuál es su puesto de trabajo?'
                }
            ),
            'position': forms.Select(
                attrs={
                    'class': 'form__input',
                    'placeholder': 'Seleccione su cargo'
                }
            ),
            'image': forms.ClearableFileInput(
                attrs={
                    'class': 'form__input-image',
                }
            ),
            'active': forms.CheckboxInput(
                attrs={
                    'class': 'form__input',
                }
            )
        }
