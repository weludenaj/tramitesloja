from django import forms
from django.forms import widgets

from .models import Direcciones


class DireccionesForm(forms.ModelForm):

    class Meta:
        model = Direcciones
        fields = ['direccion', 'tipos', 'categoria', 'equipo', 'switch', 'puerto',
                  'dependencia', 'empleado', 'observacion', 'estado', 'macaddress', 'id']
        # fields = ('__all__')
        labels = {'direccion': "Ingrese Direccion IP",
                  'estado': "Estado",
                  'macaddress': "Ingrese MAC"}
        widgets = {'direccion': forms.TextInput(
            attrs={
                'placeholder': 'Ingrese  Direccion Ip: 192.168.1.12'
            }
        ),
            'estado': forms.CheckboxInput,
            'macaddress': forms.TextInput(
            attrs={
                'placeholder': 'Ingrese  MAC: 00:00:00:00:00:00'}),
        }

    def clean_puerto(self):
        puerto = self.cleaned_data['puerto']
        if puerto > 48:
            raise forms.ValidationError('Ingrese un numero menor a 48')
        return puerto

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
# ('direccion', 'tipos', 'categoria', 'macaddress', 'equipo', 'switch', 'puerto', 'dependencia', 'empleado', 'observacion', 'objects', )
