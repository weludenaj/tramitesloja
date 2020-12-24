from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Dependencia(models.Model):
    nombre = models.CharField(verbose_name="Dependencia", max_length=250)
    class Meta:
        verbose_name = 'Dependencia'
        verbose_name_plural = 'Dependencias'
        ordering = ['nombre']
    
    def __str__(self):
        return self.nombre


class rinternos(models.Model):
    secuencia=models.PositiveIntegerField(default=0)
    fechaingreso=models.DateField(null=False, blank=False, verbose_name="Fecha")
    guianro=models.CharField(max_length=40, verbose_name="Nro Memo/Oficio", null=True, blank=True)
    remite=models.CharField(max_length=200, verbose_name="Remitente", null=False, blank=False)
    dependencia = models.CharField(max_length=250, verbose_name="Dependencia", default="Externa", null=True)
    #dependencias = models.ManyToManyField(Dependencia)
    descripcion=models.TextField(max_length=500, verbose_name="Descripcion", null=False, blank=False)
    nrotramite=models.CharField(max_length=30, verbose_name="Tramite Interno", null=True, blank=True)
    fechadespacho=models.DateField(null=True, blank=True, verbose_name="Fecha Despacho")
    enviadoa=models.TextField(null=True, blank=True,max_length=250, verbose_name="Enviado a")
    observacion=RichTextField(null=True, blank=True,max_length=500, verbose_name="Observacion")
    atendido=models.BooleanField('Atendido', default=False)
    documentos=models.FileField(upload_to='media', blank=True, null=True)

    class Meta:
        verbose_name = 'Tramite Internos'
        verbose_name_plural = 'Tramites Internos'
        ordering = ['-fechaingreso']
      ##  unique_together =('fechaingreso', 'guianro')
    def __str__(self):
        return 'Secuencia %s Fecha %s Guia %s Remitente %s Dependencias %s Descripcion %s Tramite/Oficio %s Entregado %s Enviado a %s Observacion %s Atendido %s' % (
          self.secuencia, self.fechaingreso,self.guianro, self.remite, self.dependencia, self.descripcion, self.nrotramite, self.fechadespacho, self.enviadoa, self.observacion, self.atendido )

