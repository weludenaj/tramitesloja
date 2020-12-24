import datetime

from django.db import models
from django.db.models import Q
class ExternoManager(models.Manager):
    """ managers para el model Externo """

    # def listar_externos(self):

    #     return self.all()
    
    def buscar_externos(self, kword):

        resultado = self.filter(
            usuario__icontains=kword
            )
        return resultado
    
    def buscar_externos2(self, kword):

        resultado = self.filter(
            Q(usuario__icontains=kword) | Q(guianro__icontains=kword)

            ).order_by('usuario', 'guianro', 'fechaingreso')
        return resultado

    def buscar_externos3(self, kword,f1, f2):
        date1 = datetime.datetime.strptime(f1, "%Y-%m-%d").date()
        date2 = datetime.datetime.strptime(f1, "%Y-%m-%d").date()
        resultado = self.filter(
            Q(usuario__icontains=kword) | Q(guianro__icontains=kword),
            fechaingreso__range=(date1, date2),

            ).order_by('usuario', 'guianro', 'fechaingreso')
        return resultado
