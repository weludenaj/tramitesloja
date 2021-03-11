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
    list_display = ("fecha", "empresa", "tecnico", "pozo",
                    "ingreso", "salida", "Tiempo", "PozosDetalle", "observacion")
    # fields = [("fecha", "empresa"), "direccion", "tecnico",
    #   "ingreso", "salida", "observacion"]
    #list_editable = ("salida", "observacion")
    fieldsets = (
        (None, {
            'fields': [("fecha", "empresa"), ("pozo", "tecnico"), ]
        }),
        ('Registro', {
            'fields': [("ingreso", "salida"), "observacion"]
        }),

    )
    search_fields = ("fecha", "empresa__empresa", "direccion__direccion", "tecnico", "ingreso",
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
        Tiempo.short_description = 'Estancia'

    def direc(self, obj):
        pozo_id = obj.pozo_id
        print(pozo_id)
        direccion = pozos.objects.filter(
            id=pozo_id
        ).values_list('direccion_id')
        return direccion[0]

    def PozosDetalle(self, obj):
        direccion_id = obj.direccion_id

        lista = pozos.objects.filter(
            direccion__id=direccion_id
        ).values_list(
            'numero', 'direccion_id',
        )
        listas = ''
        # print(lista)
        for p in lista:
            listas = p[0] + ' , ' + listas

        return listas
        PozosDetalle.short_description = 'Incluye Pozos'

    def save_model(self, request, obj, form, change):
        # print(obj.uc)
        pozo_id = obj.pozo_id

        direccion = pozos.objects.filter(
            id=pozo_id
        ).values_list('direccion_id')
       # print(direccion['id'])
       # print(type(direccion))
        ipdireccion = 0
        for p in direccion:
            ipdireccion = p[0]
        # print(ipdireccion)
        obj.direccion_id = ipdireccion

        obj.save()


admin.site.site_header = 'Municipio de Loja 2020'
admin.site.register(empresas, empresasAdmin)
admin.site.register(direcciones, direccionesAdmin)
admin.site.register(pozos, pozosAdmin)
admin.site.register(bitacora, bitacoraAdmin)

# admin.site.unregister(Group)
