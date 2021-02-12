from django.contrib import admin

from django.contrib.auth.models import Group, User
from datetime import datetime, date, time, timedelta

# Register your models here.
from .models import (
    empresas,
    direcciones,
    pozos,
    bitacora
)


class empresasAdmin(admin.ModelAdmin):
    list_display = ("empresa", "direccion", "contacto", "telefono")
    search_fields = ("empresa", "direccion", "contacto", "telefono")
    # list_filter=("fechaingreso",)
    # date_hierarchy="fechaingreso"


class direccionesAdmin(admin.ModelAdmin):
    list_display = ("direccion",)
    search_fields = ("direccion",)
    # list_filter=("fechaingreso",)
    # date_hierarchy="fechaingreso"


class pozosAdmin(admin.ModelAdmin):
    list_display = ("numero", "direccion", "posicion", "tipos", "observacion")
    search_fields = ("numero", "observacion")
    list_filter = ("direccion",)


class bitacoraAdmin(admin.ModelAdmin):
    list_display = ("fecha", "empresa", "direccion", "tecnico",
                    "ingreso", "salida", "Tiempo", "PozosDetalle", "observacion")
    search_fields = ("fecha", "tecnico", "ingreso",
                     "salida", "observacion", )
    date_hierarchy = "fecha"

    def Tiempo(self, obj):
        entrada = obj.ingreso
        salida = obj.salida
        dia = obj.fecha
        sentrada = entrada.strftime("%H:%M:%S")
        format_hora = "%H:%M:%S"
        if salida:
            ssalida = salida.strftime("%H:%M:%S")
            he = datetime.strptime(sentrada, format_hora)
            hs = datetime.strptime(ssalida, format_hora)
        # print("type of date_object =", type(he))
            tiempo = hs-he

        else:
            ssalida = "00:00:00"
            tiempo = '---'
        # ssalida = salida.strftime("%H:%M:%S")
        # print(ssalida)
        return tiempo

    def PozosDetalle(self, obj):
        direccion_id = obj.direccion_id

        lista = pozos.objects.filter(
            direccion__id=direccion_id
        )
        listas = ''
        for p in lista:
            listas = p.numero + ' , ' + listas

        return listas


admin.site.site_header = 'Municipio de Loja 2020'
admin.site.register(empresas, empresasAdmin)
admin.site.register(direcciones, direccionesAdmin)
admin.site.register(pozos, pozosAdmin)
admin.site.register(bitacora, bitacoraAdmin)

# admin.site.unregister(Group)
