from django.contrib import admin

from django.contrib.auth.models import Group, User


# Register your models here.
from .models import (
    empresas,
    direcciones,
    pozos,
    bitacora
)


class empresasAdmin(admin.ModelAdmin):
    list_display=("empresa","direccion","contacto","telefono")
    search_fields=("empresa", "direccion", "contacto", "telefono") 
    #list_filter=("fechaingreso",)
    #date_hierarchy="fechaingreso" 
    
class direccionesAdmin(admin.ModelAdmin):
    list_display=("direccion",)
    search_fields=("direccion",) 
    #list_filter=("fechaingreso",)
    #date_hierarchy="fechaingreso"

class pozosAdmin(admin.ModelAdmin):
    list_display=("numero","direccion", "posicion","tipos","observacion")
    search_fields=("numero", "observacion")  

class bitacoraAdmin(admin.ModelAdmin):
    list_display=("fecha", "empresa", "direccion", "ingreso", "salida", "observacion")
    search_fields=("fecha", "empresa", "direccion", "ingreso", "salida", "observacion")
    date_hierarchy="fecha"

admin.site.site_header = 'Municipio de Loja 2020' 
admin.site.register(empresas, empresasAdmin)
admin.site.register(direcciones, direccionesAdmin)
admin.site.register(pozos, pozosAdmin)
admin.site.register(bitacora, bitacoraAdmin)

#admin.site.unregister(Group)