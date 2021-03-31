from django import forms
from ckeditor.fields import RichTextField
from ckeditor.widgets import CKEditorWidget
from .models import CableadoDispersion, Dispersion, CableadoTroncal


from ckeditor.fields import RichTextField
from ckeditor.widgets import CKEditorWidget


class CableadoDispersionForm(forms.ModelForm):
    """Form definition for RegistroForm."""
    fechaingreso = forms.DateInput()
#('empresa', 'fechaingreso', 'metrajetotal', 'costo', 'total', 'observacion', )

    class Meta:
        """Meta definition for Pruebaform."""

        model = CableadoDispersion
        exclude = ['um', 'fm', 'uc', 'fc']
        fields = (
            'empresa',
            'fechaingreso',
            'metrajetotal',
            'costo',
            'total',
            'observacion',
        )
        # widgets = {
        #     # 'fechaingreso': forms.DateInput(format='%d/%m/%Y'),
        #     'usuario': forms.TextInput(
        #         attrs={
        #             'placeholder': 'Ingrese Usuario',
        #             'size': 80,
        #         }
        #     ),
        #     'guianro': forms.TextInput(
        #         attrs={
        #             'placeholder': 'Número de Trámite'
        #         }
        #     ),
        #     'descripcion': forms.Textarea(
        #         attrs={
        #             'placeholder': 'Ingrese descripción',
        #             'rows': 4,
        #             'cols': 80,
        #         }
        #     ),
        #     'enviadoa': forms.Textarea(
        #         attrs={
        #             'placeholder': 'Ingrese a quién se envió',
        #             'rows': 5,
        #             'cols': 80,
        #         }
        #     ),
        #     'observacion': forms.CharField(
        #         widget=CKEditorWidget()
        #     ),
        # }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        self.fields['empresa'].widget.attrs['readonly'] = True

    def clean_fecha(self):
        fecha = self.clean_data['fechaingreso']
        if fecha > datenow():
            raise forms.ValidationError('Fecha Incorrecta')
        return fecha
