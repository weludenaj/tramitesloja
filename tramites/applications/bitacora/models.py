from django.db import models
from django.db.models.fields.related import ForeignKey

from .managers import pozosManager

# # Create your models here.


class empresas(models.Model):
    empresa = models.CharField(verbose_name="Empresa", max_length=150)
    direccion = models.CharField(verbose_name="Direccion", max_length=250)
    contacto = models.CharField(verbose_name="Contacto", max_length=250)
    telefono = models.CharField(verbose_name="Telefono", max_length=50)

    class Meta:
        verbose_name = 'Empresas'
        verbose_name_plural = 'Empresas'
        ordering = ['-empresa']
        ##  unique_together =('fechaingreso', 'guianro')

    def __str__(self):
        return self.empresa


class direcciones(models.Model):
    direccion = models.CharField(verbose_name="Direccion", max_length=250)

    class Meta:
        verbose_name = 'Direcciones'
        verbose_name_plural = 'Direcciones'
        ordering = ['direccion', ]
##  unique_together =('fechaingreso', 'guianro')

    def __str__(self):
        return self.direccion


class pozos(models.Model):
    ubicacion = [
        ("1", "ESTE"),
        ("2", "OESTE"),
        ("3", "SUR"),
        ("4", "NORTE"),
        ("5", "SUROESTE"),
        ("6", "SURESTE"),
        ("7", "NORESTE"),
        ("8", "NOROESTE"),
    ]
    tipo = [
        ("1", "REVISION"),
        ("2", "PASO"),
    ]
    numero = models.CharField(("Numero"), max_length=50)
    direccion = models.ForeignKey(
        direcciones,
        on_delete=models.CASCADE,
        default=1,
        help_text="Escoja la direccion",
        related_name='direccion_pozo',
    )

    posicion = models.CharField(
        verbose_name="Posicion",
        choices=ubicacion,
        max_length=1,
        default="1"
    )
    tipos = models.CharField(
        verbose_name="Tipo de Pozo",
        choices=tipo,
        max_length=1,
        default="1"
    )
    observacion = models.TextField(
        verbose_name="Observacion", blank=True, null=True)
    objects = pozosManager()

    class Meta:
        verbose_name = 'Pozos'
        verbose_name_plural = 'Pozos'
        ordering = ['-numero', 'direccion', ]
    ##  unique_together =('fechaingreso', 'guianro')

    def __str__(self):
        return '{} : {} : {}'.format(self.numero, self.direccion, self.id)


class bitacora(models.Model):

    fecha = models.DateField(null=False, blank=False, verbose_name="Fecha")
    empresa = models.ForeignKey(empresas, on_delete=models.CASCADE, default=1)
    direccion = models.ForeignKey(
        direcciones, on_delete=models.CASCADE, default=1)
    tecnico = models.CharField(
        verbose_name="Asignado", max_length=250, null=True, blank=True)
    ingreso = models.TimeField(
        verbose_name='Ingresa a', auto_now=False, auto_now_add=False)
    salida = models.TimeField(
        verbose_name='Sale a', auto_now=False, auto_now_add=False, null=True, blank=True,)
    pozo = models.ForeignKey(pozos, on_delete=models.CASCADE, default=170)
    observacion = models.TextField(
        verbose_name='Observaciones', null=True, blank=True)

    class Meta:
        verbose_name = 'Bitacora'
        verbose_name_plural = 'Bitacora'
        ordering = ['-fecha']
    ##  unique_together =('fechaingreso', 'guianro')

    def __str__(self):
        return 'Fecha %s Empresa %s Direccion %s Ingreso a %s Salida a %s Observacion %s' % (self.fecha, self.empresa, self.direccion, self.ingreso, self.salida, self.observacion)
