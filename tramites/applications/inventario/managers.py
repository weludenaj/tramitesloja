
from django.db import models
from django.db.models import Q


class DireccionesManager(models.Manager):
    """manageres para el model direcciones """

    def buscar_ip(self, kword):
        resultado = self.filter(
            Q(direccion__icontains=kword) | Q(observacion__icontains=kword) | Q(
                direccion__dependencia=kword) | Q(direccion__empleado=kword)
        )
        return resultado

    # Funcion para excluir algo en la busqueda

    def buscar_ip1(self, kword):
        resultado = self.filter(
            Q(direccion__icontains=kword) | Q(observacion__icontains=kword) | Q(direccion__icontains=kword) | Q(observacion__icontains=kword) | Q(
                dependencia__dependencia__icontains=kword) | Q(empleado__nombres__icontains=kword)
        ).exclude(id=1).order_by('id')
        return resultado

    def listar_ips_empleado(self, empleado):

        return self.filter(
            Empleado__id=empleado
        ).order_by('direccion')


class EmpleadosManager(models.Manager):

    def buscar_empleados(self, kword):
        resultado = self.filter(
            Q(cedula__icontains=kword) | Q(nombres__icontains=kword) | Q(
                correo__icontains=kword) | Q(cargo__icontains=kword)
        ).exclude(id=1)
        return resultado

    def empleado_por_ip(self, direcciones):

        return self.filter(
            empleado_direccion__empleado__id=direcciones
        )


class SwitchesManager(models.Manager):
    #('nombre', 'puertos', 'rack', 'marca', 'modelo', 'serial=models.CharField(verbose_name', 'mac', )
    def buscar_switches(self, kword):
        resultado = self.filter(
            Q(nombre__icontains=kword) | Q(
                marca__icontains=kword) | Q(mac__icontains=kword)
        ).exclude(id=1)
        return resultado
