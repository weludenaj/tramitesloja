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
    list_filter = ("area", "estado")
    # date_hierarchy="fechaingreso"


class TramitesInformaticaAdmin(admin.ModelAdmin):

    list_display = ('fecha', 'guianro', 'usuario', 'dependencia', 'asunto', 'descripcions',
                    'asignado', 'fechaasignado', 'fechaatendido', 'observacion', 'fase', )
    #list_display_links = ('fecha', 'guianro')
    #list_display_links = None
    fields = [('fecha', 'guianro'), ('usuario', 'dependencia'), ('asunto', 'descripcion'),
              ('asignado', 'fechaasignado', 'fechaatendido'), ('observacion', 'fase'), ]
    search_fields = ('guianro', 'usuario', 'dependencia__dependencia', 'asunto', 'descripcion',
                     'asignado__nombre', 'fechaasignado', 'fechaatendido', 'observacion', 'fase', )
    date_hierarchy = 'fecha'
    readonly_fields = ('um', 'uc')
    list_filter = ('fase',)
    list_per_page = 5

    def descripcions(self, obj):
        descrip = obj.descripcion
        descrip = descrip[0:150]
        # print(descrip)
        return descrip

    # def dependencia1(self, obj):
    #     # print(obj.dependencia.dependencia)
    #     dep = obj.dependencia.dependencia
    #     dep = dep[:30]
    #     return dep  # obj.dependencia[0:30]

    # def Tiempo(self, obj):
    #     entrada = obj.fechaasignado
    #     salida = obj.fechaatendido
    #     dia = obj.fecha
    #     sentrada = entrada.strftime("%d:%m:%Y")
    #     format_hora = "%d:%m:%Y"
    #     if salida:
    #         ssalida = salida.strftime("%d:%m:%Y")
    #         he = datetime.strptime(sentrada, format_hora)
    #         hs = datetime.strptime(ssalida, format_hora)
    #     # print("type of date_object =", type(he))
    #         tiempo = hs-he

    #     else:
    #         ssalida = "00:00:00"
    #         tiempo = '---'
    #     # ssalida = salida.strftime("%H:%M:%S")
    #     # print(ssalida)
    #     return tiempo

    def save_model(self, request, obj, form, change):
        # print(obj.uc)

        if obj.uc_id == None:
            obj.uc_id = request.user.id
        if request.user.id != 1:
            obj.um = request.user.id

        obj.save()


admin.site.register(Informatica, InformaticaAdmin)
admin.site.register(TramitesInformatica, TramitesInformaticaAdmin)
