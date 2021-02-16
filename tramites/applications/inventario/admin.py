from .models import (
    Switches,
    TipoDireccion,
    Categorias,
    Direcciones,
    Empleados,
    Dependencias,
)
from enum import unique
from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import Group, User
from datetime import datetime, date, time, timedelta


# class ClaseModelo(models.Model):
#     estado = models.BooleanField(default=True)
#     fc = models.DateTimeField(auto_now_add=True)
#     fm = models.DateTimeField(auto_now=True, blank=True, null=True)
#     uc = models.ForeignKey(User, on_delete=models.CASCADE)
#     um = models.IntegerField(blank=True, null=True)


# Register your models here.


class SwitchesAdmin(admin.ModelAdmin):
    list_display = ("nombre", "puertos", "rack", "marca", "ip", "mac")
    search_fields = ("nombre", "rack", "marca", "ip", "mac")
    # list_filter=("fechaingreso",)
    # date_hierarchy="fechaingreso"


class TipoDireccionAdmin(admin.ModelAdmin):
    list_display = ("tipo",)
    search_fields = ("tipo",)
    # list_filter=("fechaingreso",)
    # date_hierarchy="fechaingreso"


class CategoriasAdmin(admin.ModelAdmin):
    list_display = ("categoria",)
    search_fields = ("categoria",)


class DependenciasAdmin(admin.ModelAdmin):
    list_display = ("dependencia",)
    search_fields = ("dependencia",)


class EmpleadosAdmin(admin.ModelAdmin):
    list_display = ("nombres", "cedula", "correo", "extension",  "cargo")
    search_fields = ("nombres", "cedula", "cargo")


class DireccionesAdmin(admin.ModelAdmin):
    list_display = ("direccion", "tipos", "categoria", "macaddress",
                    "equipo", "switch", "dependencia", "empleado", "observacion")
    search_fields = ("direccion", "macaddress", "equipo",
                     "observacion", "empleado__nombres", "dependencia__dependencia", "switch__nombre")
    readonly_fields = ('um', 'uc')

    def save_model(self, request, obj, form, change):
        print(obj.um)
        print(request.user.id)
        if request.user.id != 1:
            obj.um = request.user.id
        obj.save()


admin.site.site_header = 'Municipio de Loja 2020-2021 - Direccion de Tecnologia'
#admin.site.site_title = 'Alcaldia Loja'
admin.site.index_title = 'Alcaldia Loja'
admin.site.register(Switches, SwitchesAdmin)
admin.site.register(Categorias, CategoriasAdmin)
admin.site.register(TipoDireccion, TipoDireccionAdmin)
admin.site.register(Empleados, EmpleadosAdmin)
admin.site.register(Dependencias, DependenciasAdmin)
admin.site.register(Direcciones, DireccionesAdmin)

# admin.site.unregister(Group)
