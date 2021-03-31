
from django.db import models
from django.db.models import Q


class DucteriaManager(models.Manager):
    """manageres para el model Dispersion """
#('empresa', 'fechaingreso', 'metrajetotal', 'costo', 'total', 'observacion', )

    def buscar(self, kword):
        resultado = self.filter(
            Q(observacion__icontains=kword)
        )
        return resultado
