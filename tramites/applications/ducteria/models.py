from django.db import models

from applications.inventario.models import ClaseModelo
from applications.bitacora.models import direcciones, empresas, pozos
# Create your models here.

#from .applications.inventario.models import Empleados, Dependencias
from django.contrib.auth.models import User
from django.db.models.fields import CharField, EmailField


# Create your models here.


from django.db.models.fields.related import ForeignKey

from .managers import DucteriaManager

# # Create your models here.


class Costos(ClaseModelo):
    costo = models.FloatField(
        verbose_name="Costo Definido", blank=False, null=False)
    fecha = models.DateField(verbose_name="Fecha Inicio",
                             auto_now=False, auto_now_add=False, blank=False, null=False)
    observacion = models.TextField(verbose_name="Observacion")

    class Meta:
        verbose_name = 'Costo Definido '
        verbose_name_plural = 'Costos Definidos'
        ordering = ['-fecha']
        ##  unique_together =('fechaingreso', 'guianro')

    def __str__(self):
        return '{} : {}'.format(self.costo, self.fecha)


class Predios(ClaseModelo):
    predio = models.CharField(verbose_name="Predio", max_length=50)
    direccion = models.ForeignKey(
        direcciones,
        on_delete=models.CASCADE,
        default=1,
        help_text="Escoja la direccion",
        related_name='direccion_predio'
    )
    propietario = models.CharField(verbose_name="Propietario", max_length=150)

    class Meta:
        verbose_name = 'Predios'
        verbose_name_plural = 'Predios'
        ordering = ['direccion', 'predio']
        ##  unique_together =('fechaingreso', 'guianro')

    def __str__(self):
        return '{} : {} : {}'.format(self.predio, self.direccion, self.propietario)


class Infraestructura(ClaseModelo):
    descripcion = models.CharField(verbose_name="Detalle", max_length=250)
    empresa = models.ForeignKey(empresas, on_delete=models.CASCADE)
    pozo = models.ForeignKey(pozos, on_delete=models.CASCADE)
    observacion = models.TextField(verbose_name="Observacion", default='')

    class Meta:
        verbose_name = 'Infraestructura'
        verbose_name_plural = 'Infraestructura'
        ordering = ['empresa', 'pozo']
        ##  unique_together =('fechaingreso', 'guianro')

    def __str__(self):
        return '{} : {} : {}'.format(self.descripcion, self.empresa, self.pozo)


class CableadoTroncal(ClaseModelo):
    empresa = models.ForeignKey(empresas, on_delete=models.CASCADE)
    fechaingreso = models.DateField(
        verbose_name='Fecha de Registro', auto_now=False, auto_now_add=False)
    nombreruta = models.CharField(
        verbose_name='Nombre de la Ruta', max_length=250)
    descripcion = models.TextField(verbose_name='Descripcion de la Ruta')
    inicio = models.FloatField(
        verbose_name='Metraje Inicial')
    final = models.FloatField(
        verbose_name='Metraje Final')
    total = models.FloatField(verbose_name='Total'
                              )
    costo = models.ForeignKey(Costos, on_delete=models.CASCADE)
    observacion = models.TextField(verbose_name='Observacion', default='')

    class Meta:
        verbose_name = 'Cableado Troncal '
        verbose_name_plural = 'Cableado Troncal'
        ordering = ['-fechaingreso']
        ##  unique_together =('fechaingreso', 'guianro')

    def __str__(self):
        return '{} : {} : {} : {}: {}'.format(self.empresa, self.fechaingreso, self.nombreruta, self.total, self.costo)

    def save(self):
        self.nombreruta = self.nombreruta.upper()
        self.total = abs(self.inicio - self.final)
        super(CableadoTroncal, self).save()


class CableadoDispersion(ClaseModelo):
    empresa = models.ForeignKey(empresas, on_delete=models.CASCADE)
    fechaingreso = models.DateField(
        verbose_name='Fecha de Registro', auto_now=False, auto_now_add=False)
    metrajetotal = models.FloatField(verbose_name='Metraje Total')
    costo = models.ForeignKey(Costos, on_delete=models.CASCADE)
    total = models.FloatField(verbose_name='Total')
    observacion = models.TextField(verbose_name='Observacion', default='')

    objects = DucteriaManager()

    class Meta:
        verbose_name = 'Cableado Dispersion '
        verbose_name_plural = 'Cableado Dispersion'
        ordering = ['-fechaingreso']
        ##  unique_together =('fechaingreso', 'guianro')

    def __str__(self):
        return '{} : {} : {} : {}: {}'.format(self.empresa, self.fechaingreso, self.metrajetotal, self.costo, self.total)

    def save(self):
        self.total = self.metrajetotal * self.costo.costo
        super(CableadoDispersion, self).save()


class Dispersion(ClaseModelo):

    operaciones = [
        (1, 'Instalacion'),
        (2, 'Desinstalacion'),
    ]
    dispersion = models.ForeignKey(
        CableadoDispersion, on_delete=models.CASCADE)
    instalado = models.DateField(
        verbose_name='Fecha de Instalacion', auto_now=False, auto_now_add=False)
    cliente = models.CharField(verbose_name='Beneficiario', max_length=250)
    direccion = models.ForeignKey(direcciones, on_delete=models.CASCADE)
    origen = models.ForeignKey(
        Infraestructura,
        on_delete=models.CASCADE,
        related_name='CableadoDispersion',
        related_query_name='cableadodispersion')
    destino = models.ForeignKey(Predios, on_delete=models.CASCADE)
    ruta = models.TextField(verbose_name='Descripion de la Ruta por Pozo')
    inicio = models.FloatField(verbose_name='Metraje Inicial')
    final = models.FloatField(verbose_name=' Metraje Final')
    total = models.FloatField(verbose_name='Total')
    costo = models.ForeignKey(Costos, on_delete=models.CASCADE)
    totalpago = models.FloatField(verbose_name='Total a Pagar')
    operacion = models.PositiveIntegerField(
        verbose_name='Operacion', choices=operaciones, default=1)
    observacion = models.TextField(verbose_name='Observacion', default='')

    class Meta:
        verbose_name = 'Detalle Dispersion '
        verbose_name_plural = 'Detalle Dispersion'
        ordering = ['-dispersion']
        ##  unique_together =('fechaingreso', 'guianro')

    def __str__(self):
        return '{} : {} : {} : {}: {}'.format(self.dispersion, self.instalado, self.cliente, self.total, self.totalpago)

    # def formfield_for_foreignkey(self, db_field, request, **kwargs):
    #     if db_field.name == 'origen':
    #         kwargs['queryset'] = Infraestructura.objects.filter(empresa='S').order_by('nombre')
    #     return super(ConsumerAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def save(self):
        self.total = abs(self.inicio - self.final)
        self.totalpago = self.total * self.costo.costo
        super(Dispersion, self).save()
