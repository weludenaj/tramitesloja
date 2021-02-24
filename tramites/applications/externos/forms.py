from django import forms
from ckeditor.fields import RichTextField
from ckeditor.widgets import CKEditorWidget
from .models import rexternos


from ckeditor.fields import RichTextField
from ckeditor.widgets import CKEditorWidget


class RegistroForm(forms.ModelForm):
    """Form definition for RegistroForm."""

    class Meta:
        """Meta definition for Pruebaform."""

        model = rexternos
        fields = (
            'fechaingreso',
            'guianro',
            'usuario',
            'descripcion',
            'oficio',
            'fechaentrega',
            'enviadoa',
            'observacion',
            'atendido',
        )
        widgets = {
            # 'fechaingreso': forms.DateInput(format='%d/%m/%Y'),
            'usuario': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese Usuario',
                    'size': 80,
                }
            ),
            'guianro': forms.TextInput(
                attrs={
                    'placeholder': 'Número de Trámite'
                }
            ),
            'descripcion': forms.Textarea(
                attrs={
                    'placeholder': 'Ingrese descripción',
                    'rows': 4,
                    'cols': 80,
                }
            ),
            'enviadoa': forms.Textarea(
                attrs={
                    'placeholder': 'Ingrese a quién se envió',
                    'rows': 5,
                    'cols': 80,
                }
            ),
            'observacion': forms.CharField(
                widget=CKEditorWidget()
            ),
        }

    def clean_fecha(self):
        fecha = self.clean_data['fechaingreso']
        if fecha > datenow():
            raise forms.ValidationError('Fecha Incorrecta')
        return fecha
