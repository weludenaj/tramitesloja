from enum import unique
from django.db import models


from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE


# Create your models here.

from .managers import DireccionesManager, EmpleadosManager, SwitchesManager


class ClaseModelo(models.Model):
    estado = models.BooleanField(default=True)
    fc = models.DateTimeField(auto_now_add=True)
    fm = models.DateTimeField(auto_now=True, blank=True, null=True)
    uc = models.ForeignKey(User, on_delete=models.CASCADE)
    um = models.IntegerField(blank=True, null=True)

    class Meta:
        abstract = True


class Switches(ClaseModelo):
    nombre = models.CharField(verbose_name='Nombre del Switch', max_length=150)
    puertos = models.PositiveIntegerField(
        verbose_name='Cantidad de Puertos', default=48)
    rack = models.CharField(verbose_name='Ubicacion', max_length=150)
    marca = models.CharField(verbose_name='Marca',
                             max_length=250, null=True, blank=True)
    modelo = models.CharField(verbose_name='Modelo',
                              max_length=150, null=True, blank=True)
    serial = models.CharField(verbose_name='Serial',
                              max_length=50, null=True, blank=True)
    ip = models.CharField(verbose_name='Direccion IP',
                          max_length=15, null=True, blank=True)
    mac = models.CharField(verbose_name='Direccion Mac',
                           max_length=17, null=True, blank=True)

    objects = SwitchesManager()

    class Meta:
        verbose_name = 'Switch'
        verbose_name_plural = 'Switches'
        ordering = ['nombre', ]

    def __str__(self):
        return '{}:{}'.format(self.nombre, self.marca, self.modelo)


class TipoDireccion(models.Model):
    tipo = models.CharField(verbose_name='Tipo', max_length=50)

    class Meta:
        verbose_name = 'Tipos Dirección'
        verbose_name_plural = 'Tipos de Direcciones'
        ordering = ['tipo', ]

    def __str__(self):
        return self.tipo


class Categorias(models.Model):
    categoria = models.CharField(verbose_name='Categoria', max_length=150)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['categoria', ]

    def __str__(self):
        return self.categoria


class Dependencias(ClaseModelo):
    dependencia = models.CharField(verbose_name='Dependencia', max_length=350)

    class Meta:
        verbose_name = 'Depedencias'
        verbose_name_plural = 'Dependencias'
        ordering = ['dependencia', ]

    def __str__(self):
        return '{}'.format(self.dependencia)

    def save(self):
        self.dependencia = self.dependencia.upper()
        super(Dependencias, self).save()


class Empleados(ClaseModelo):
    cedula = models.CharField(verbose_name='Identificacion', max_length=13)
    nombres = models.CharField(
        verbose_name='Nombre', max_length=350, unique=True)
    correo = models.EmailField(
        verbose_name='Email', max_length=254, unique=True)
    extension = models.PositiveIntegerField(
        verbose_name='Extension', blank=True, null=True)
    celular = models.CharField(
        verbose_name='Celular', max_length=10, blank=True, null=True)
    cargo = models.CharField(verbose_name='Cargo',
                             max_length=250, blank=True, null=True)

    objects = EmpleadosManager()

    def __str__(self):
        return '{}:{}'.format(self.nombres, self.cargo)

    def save(self):
        self.nombres = self.nombres.upper()
        super(Empleados, self).save()

    class Meta:
        verbose_name = 'Empleados'
        verbose_name_plural = 'Empleados'
        ordering = ['nombres', ]


class Direcciones(ClaseModelo):
    estatus = [
        (1, "Activo"),
        (2, "Libre"),
        (3, "Bloqueado"),
    ]

    direccion = models.CharField(
        verbose_name='Direccion Ip',
        max_length=15,
        help_text='Ingrese direccion Ip'
    )
    tipos = models.ForeignKey(
        TipoDireccion, verbose_name='Tipo', on_delete=models.CASCADE, default=1)
    categoria = models.ForeignKey(Categorias, on_delete=CASCADE, default=1)
    macaddress = models.CharField(
        verbose_name='Direccion Mac', max_length=17, null=True, blank=True)
    equipo = models.CharField(verbose_name='Nombre del Host', max_length=50)
    switch = models.ForeignKey(Switches, on_delete=CASCADE, default=1)
    puerto = models.PositiveSmallIntegerField(
        verbose_name='Puerto', default=1, null=True, blank=True)
    dependencia = models.ForeignKey(Dependencias, on_delete=CASCADE, default=1)
    empleado = models.ForeignKey(
        Empleados, on_delete=CASCADE, default=1, related_name='empleado_direccion')
    observacion = models.TextField(verbose_name='Observacion')
    estatusip = models.IntegerField(verbose_name='Estatus', choices=estatus, default=1)
    objects = DireccionesManager()

    class Meta:
        verbose_name = 'Direcciones IPs'
        verbose_name_plural = 'Direcciones Ips'
        #ordering = ['direccion',]

    def __str__(self):
        return '{}'.format(self.direccion)

    def save(self):
        if self.macaddress != None:
            self.macaddress = self.macaddress.upper()
        super(Direcciones, self).save()


class contrasenias(ClaseModelo):
    direccion = models.ForeignKey(
        Direcciones, verbose_name='Direccion', on_delete=models.CASCADE)
    usuario = models.CharField(
        verbose_name='usuario', max_length=50, default='admin')
    contrasenia = models.CharField(
        verbose_name='Contrasena', max_length=50, default='admin')

    class Meta:
        verbose_name = 'Contraseñas'
        verbose_name_plural = 'Contraseñas'
        #ordering = ['direccion',]

    def __str__(self):
        return '{}:{}:{}'.format(self.direccion, self.usuario, self.contrasenia)
