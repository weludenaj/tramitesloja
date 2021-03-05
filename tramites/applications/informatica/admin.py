from django.contrib import admin


from django.contrib.auth.models import Group, User
from datetime import datetime, date, time, timedelta

# Register your models here.
from .models import (
    Informatica,
    TramitesInformatica,
)


class InformaticaAdmin(admin.ModelAdmin):

    list_display = ('nombre', 'area', 'correo', )
    search_fields = ('nombre', 'area', 'correo', )
    list_filter = ("area",)
    # date_hierarchy="fechaingreso"


class TramitesInformaticaAdmin(admin.ModelAdmin):

    list_display = ('fecha', 'guianro', 'usuario', 'dependencia', 'asunto', 'descripcion',
                    'asignado', 'fechaasignado', 'fechaatendido', 'observacion', 'fase', )
    search_fields = ('guianro', 'usuario', 'dependencia__dependencia', 'asunto', 'descripcion',
                     'asignado__nombre', 'fechaasignado', 'fechaatendido', 'observacion', 'fase', )
    date_hierarchy = 'fecha'


admin.site.register(Informatica, InformaticaAdmin)
admin.site.register(TramitesInformatica, TramitesInformaticaAdmin)
