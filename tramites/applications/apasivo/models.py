from django.db import models

from django.db.models.fields.related import ForeignKey

#from .managers import pozosManager

# # Create your models here.

class seriedocumental(models.Model):
    seriedocu = models.CharField(
        verbose_name = "Serie Documental",
        default = "--Ingrese Descripcion --",
        max_length = 150,
    )

    class Meta:
        verbose_name = 'Serie Documental'
        verbose_name_plural = 'Serie Documental'
        ordering = ['-id']
        ##  unique_together =('fechaingreso', 'guianro')

    def __str__(self):
        return self.seriedocu

class registropasivo(models.Model):

    destino = [
        ("1", "CONSERVACIÓN"),
        ("2", "ELIMINACIÓN"),
        ("3", "OTRO"),
    ]

    
    tiposoporte = [
        ("1", "FÍSICO"),
        ("2", "DIGITAL"),
        ("3", "MAGNÉTICO"),
        ("4", "SOPORTE"),
    ]

    tipozona = [
        ("1", "Primer Piso"),
        ("2", "Segundo Piso"),
        ("3", "Otro"),
    ]
    subseries = [
        ("1", "Enviados"),
        ("2", "Recibidos"),
        ("3", "Otros"),
    ]

    seccion = models.CharField(verbose_name="Seccion", max_length=150)
    subseccion = models.CharField(verbose_name="SubSeccion", max_length=150,default="---Ninguna ---")
    seriedocu = models.ForeignKey(
        seriedocumental,
        on_delete=models.CASCADE,
        default=1,
        help_text="Escoja la Serie Documental",
    )
    subserie = models.CharField(
        verbose_name="Subserie",
        max_length=1,  
        default = "1",
        choices = subseries,
    )
    nrocaja = models.CharField(verbose_name="Nro Caja", max_length=150)
    expediente = models.CharField(verbose_name="Nro Expediente", max_length=250)
    descripcion = models.TextField(verbose_name="Descripcion")
    apertura = models.DateField(verbose_name="Fecha Apertura")
    cierre = models.DateField(verbose_name="Fecha de Cierre")
    nrofojas = models.PositiveIntegerField(verbose_name="Nro Fojas", default=1)
    destinofinal = models.CharField(
        verbose_name = "Destino Final",
        choices = destino,
        max_length = 1,
        default ="1"
    )
    
    soporte = models.CharField(
        verbose_name="Soporte",
        choices = tiposoporte,
        default="1",
        max_length=1,
    )
    zona = models.CharField(
        verbose_name="Zona",
        choices = tipozona,
        max_length=1,
        default="1",
    )

    estanteria = models.PositiveIntegerField (verbose_name="Estanteria", default=1)
    bandeja = models.PositiveIntegerField (verbose_name="Bandeja", default = 1)
    observacion = models.TextField(verbose_name="Observaciones", null=True, blank=True)

    class Meta:
        verbose_name = 'Archivo Pasivo'
        verbose_name_plural = 'Pasivo'
        ordering = ['-id']
        ##  unique_together =('fechaingreso', 'guianro')

    def __str__(self):
        return self.descripcion


