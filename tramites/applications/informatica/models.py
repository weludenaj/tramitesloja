from django.db import models

from applications.inventario.models import ClaseModelo, Empleados, Dependencias

# Create your models here.

#from .applications.inventario.models import Empleados, Dependencias
from django.contrib.auth.models import User
from django.db.models.fields import CharField, EmailField

# Create your models here.


class Informatica(models.Model):
    estados = [
        (1, 'Activo'),
        (2, 'Inactivo'),
    ]
    nombre = models.CharField(
        max_length=150, verbose_name="Nombres", null=False, blank=False)
    area = models.CharField(
        max_length=80, verbose_name="Area", null=False, blank=False)
    correo = models.EmailField(
        verbose_name="Correo Electronico", null=False, blank=False)
    estado = models.PositiveSmallIntegerField(
        verbose_name="Estado Actual",
        default=1,
        choices=estados,
    )

    class Meta:
        verbose_name = 'Tecnicos'
        verbose_name_plural = 'Tecnicos Informaticos'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


# class ClaseModelo(models.Model):
#     estado = models.BooleanField(default=True)
#     fc = models.DateTimeField(auto_now_add=True)
#     fm = models.DateTimeField(auto_now=True, blank=True, null=True)
#     uc = models.ForeignKey(User, on_delete=models.CASCADE)
#     um = models.IntegerField(blank=True, null=True)

#     class Meta:
#         abstract = True


class TramitesInformatica(ClaseModelo):
    fases = [
        ('1', 'Ingresado'),
        ('2', 'Asignado'),
        ('3', 'Atendido'),
    ]

    fecha = models.DateField(null=False, blank=False, verbose_name="Fecha")
    guianro = models.CharField(
        max_length=30, verbose_name="Memorando Nro", null=False, blank=False, unique=False)
    usuario = models.CharField(
        max_length=200, verbose_name="Usuario", null=False, blank=False)
    dependencia = models.ForeignKey(Dependencias, on_delete=models.CASCADE)
    asunto = models.TextField(
        max_length=500, verbose_name="Asunto", null=False, blank=False)
    descripcion = models.TextField(
        verbose_name="Descripcion Breve", null=True, blank=True)
    asignado = models.ForeignKey(Informatica, on_delete=models.CASCADE)
    fechaasignado = models.DateField(
        null=True, blank=True, verbose_name="Asignado el")
    fechaatendido = models.DateField(
        verbose_name="Atendido el",
        auto_now=False,
        auto_now_add=False,
        null=True, blank=True)
    observacion = models.TextField(
        null=True, blank=True, verbose_name="Observacion")
    fase = models.CharField(
        verbose_name="Fase Tarea",
        max_length=1,
        choices=fases,
        default='1',
    )

    class Meta:
        verbose_name = 'Tramites Informatica'
        verbose_name_plural = 'Tramites Informaticos'
        ordering = ['-fecha']
      ##  unique_together =('fechaingreso', 'guianro')

    def __str__(self):
        return 'Fecha %s Guia %s Usuario %s Dependencia %s Asunto %s Descripcion %s Asignado a %s Asignado el %s Atendido el %s  Observacion %s Fase %s' % (self.fecha, self.guianro, self.usuario, self.dependencia, self.asunto, self.descripcion,
                                                                                                                                                            self.asignado, self.fechaasignado, self.fechaatendido, self.observacion, self.fase)
