from django.db import models

from django.db.models.fields.related import ForeignKey

#from .managers import pozosManager

# # Create your models here.


class registropasivo(models.Model):
    seccion = models.CharField(verbose_name="Seccion", max_length=150)
    nrocaja = models.CharField(verbose_name="Nro Caja", max_length=150)
    expediente = models.CharField(verbose_name="Nro Expediente", max_length=250)
    descripcion = models.TextField(verbose_name="Descripcion")
    apertura = models.DateField(verbose_name="Fecha Apertura")
    cierre = models.DateField(verbose_name="Fecha de Cierre")
    nrofojas = models.PositiveIntegerField(verbose_name="Nro Fojas", default=1)
    destinofinal = models.CharField(verbose_name="Destino Final", default="Conservacion", max_length=250)
    soporte = models.CharField(verbose_name="Soporte", default="Fisico", max_length=150)
    zona = models.CharField(verbose_name="Zona", max_length=150)
    estanteria = models.CharField(verbose_name="Estanteria", max_length =150)
    bandeja = models.CharField(verbose_name="Bandeja", max_length = 150)
    observacion = models.TextField(verbose_name="Observaciones", null=True, blank=True)

    class Meta:
        verbose_name = 'Archivo Pasivo'
        verbose_name_plural = 'Pasivo'
        ordering = ['-id']
        ##  unique_together =('fechaingreso', 'guianro')

    def __str__(self):
        return self.descripcion


