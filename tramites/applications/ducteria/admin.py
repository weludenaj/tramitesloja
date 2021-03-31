from django.contrib import admin

from django.contrib.auth.models import Group, User
from datetime import datetime, date, time, timedelta

from django.db import models

# Register your models here.
from .models import (
    Costos, Predios, Infraestructura, CableadoTroncal, CableadoDispersion, Dispersion
)


class CostosAdmin(admin.ModelAdmin):

    list_display = ('costo', 'fecha', 'observacion')
    search_fields = ('costo', 'observacion')
    list_filter = ("fecha",)
    # date_hierarchy="fechaingreso"


class PrediosAdmin(admin.ModelAdmin):

    list_display = ('predio', 'direccion', 'propietario', )
    #list_display_links = ('fecha', 'guianro')
    #list_display_links = None
    # fields = [('fecha', 'guianro'), ('usuario', 'dependencia'), ('asunto', 'descripcion'),
    #          ('asignado', 'fechaasignado', 'fechaatendido'), ('observacion', 'fase'), ]
    search_fields = ('predio', 'direccion__direccion', 'propietario',)
    #date_hierarchy = 'fecha'
    readonly_fields = ('um', 'uc')
    #list_filter = ('fase',)
    list_per_page = 20

    def save_model(self, request, obj, form, change):
        # print(obj.uc)

        if obj.uc_id == None:
            obj.uc_id = request.user.id
        if request.user.id != 1:
            obj.um = request.user.id

        obj.save()


class InfraestructuraAdmin(admin.ModelAdmin):
    list_display = ('descripcion', 'empresa', 'pozo', 'observacion')
    search_fields = ('descripcion', 'empresa__empresa',
                     'pozo__numero', 'observacion')
    list_filter = ('empresa',)
    readonly_fields = ('um', 'uc')
    list_per_page = 20

    def save_model(self, request, obj, form, change):
        # print(obj.uc)

        if obj.uc_id == None:
            obj.uc_id = request.user.id
        if request.user.id != 1:
            obj.um = request.user.id

        obj.save()


class CableadoTroncalAdmin(admin.ModelAdmin):
    list_display = ('empresa', 'fechaingreso', 'nombreruta', 'descripcion',
                    'inicio', 'final', 'total', 'costo', 'observacion')
    search_fields = ('empresa__empresa', 'nombreruta',
                     'descripcion', 'observacion')
    list_filter = ('empresa',)
    readonly_fields = ('um', 'uc')
    list_per_page = 20
    date_hierarchy = 'fechaingreso'

    def save_model(self, request, obj, form, change):
        # print(obj.uc)

        if obj.uc_id == None:
            obj.uc_id = request.user.id
        if request.user.id != 1:
            obj.um = request.user.id

        obj.save()


class CableDispersionAdmin(admin.ModelAdmin):
    list_display = ('empresa', 'fechaingreso', 'metrajetotal',
                    'costo', 'total', 'observacion')
    search_fields = ('empresa__empresa',)
    list_filter = ('empresa',)
    readonly_fields = ('um', 'uc')
    list_per_page = 20
    date_hierarchy = 'fechaingreso'

    def save_model(self, request, obj, form, change):
        # print(obj.uc)

        if obj.uc_id == None:
            obj.uc_id = request.user.id
        if request.user.id != 1:
            obj.um = request.user.id

        obj.save()


class DispersionAdmin(admin.ModelAdmin):
    list_display = ('dispersion', 'instalado', 'cliente', 'direccion', 'origen', 'destino',
                    'ruta', 'inicio', 'final', 'total', 'costo', 'totalpago', 'operacion', 'observacion')
    search_fields = ('cliente', 'direccion__direccion', 'observacion')
    list_filter = ('operacion',)
    readonly_fields = ('um', 'uc')
    list_per_page = 20
    date_hierarchy = 'instalado'

    # def formfield_for_foreignkey(self, db_field, request, **kwargs):
    #     if db_field.name == 'origen':
    #         kwargs['queryset'] = Infraestructura.objects.filter(empresa='S').order_by('nombre')
    #     return super(ConsumerAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def save_model(self, request, obj, form, change):
        # print(obj.uc)

        if obj.uc_id == None:
            obj.uc_id = request.user.id
        if request.user.id != 1:
            obj.um = request.user.id

        obj.save()


# class DispersionInLine(admin.StackedInline):
#     model = Dispersion
#     can_delete = False
#     verbose_name_plural = 'Detalle'


# class CableadoDispersionDetalleAdmin(CableDispersionAdmin):
#     inlines = (DispersionInLine,)
# #     list_display = (
# #         'dispersion', 'instalado', 'cliente', 'direccion', 'origen', 'destino',
# #         'ruta', 'inicio', 'final', 'total', 'costo', 'totalpago', 'operacion', 'observacion'
# #     )


admin.site.register(Costos, CostosAdmin)
admin.site.register(Predios, PrediosAdmin)
admin.site.register(Infraestructura, InfraestructuraAdmin)
admin.site.register(CableadoTroncal, CableadoTroncalAdmin)
admin.site.register(CableadoDispersion, CableDispersionAdmin)
admin.site.register(Dispersion, DispersionAdmin)
# admin.site.unregister(CableadoDispersion)
# admin.site.register(CableadoDispersionDetalleAdmin)
