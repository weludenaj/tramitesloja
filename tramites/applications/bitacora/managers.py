
from django.db import models
from django.db.models import Q


# class DireccionesManager(models.Manager):
#     """manageres para el model direcciones """

#     def buscar_ip(self, kword):
#         resultado = self.filter(
#             Q(direccion__icontains=kword) | Q(observacion__icontains=kword)
#         )
#         return resultado

#     # Funcion para excluir algo en la busqueda

#     def buscar_ip1(self, kword):
#         resultado = self.filter(
#             Q(direccion__icontains=kword) | Q(observacion__icontains=kword)
#         ).exclude(id=1)
#         return resultado


# class EmpleadosManager(models.Manager):

#     def buscar_empleados(self, kword):
#         resultado = self.filter(
#             Q(cedula__icontains=kword) | Q(nombres__icontains=kword) | Q(
#                 correo__icontains=kword) | Q(cargo__icontains=kword)
#         ).exclude(id=1)
#         return resultado


class pozosManager(models.Manager):

    def buscar_pozos(self, kword):
        resultado = self.filter(
            Q(numero__icontains=kword) | Q(observacion__icontains=kword)
        )
        return resultado

    def pozos_por_direccion(self, direccion):
        return self.filter(
            direccion_pozo__direccion_id=direccion
        )

    def listar_pozos_direccion(self, kword):

        return self.filter(
            direccion__id=kword
        ).order_by('numero')
