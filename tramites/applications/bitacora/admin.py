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
    list_display=("fecha", "empresa", "direccion", "tecnico", "ingreso", "salida", "observacion")
    search_fields=("fecha", "tecnico", "ingreso", "salida", "observacion")
    date_hierarchy="fecha"
    
    # def post_calculo(self, obj):
    #     entrada = obj.ingreso
    #     salida = obj.salida
    #     format_hora="%H : %M: %S"
    #     print (entrada)
    #     print (salida)
    #     then1 = datetime.strptime("07:17:20","%H:%M:%S")
    #     print('type of date_object =', type(then1))
    #     #print("type of date_object =", type(entrada))
    #     #tiempo= salida.Subtract(entrada).TotalHours;
    #     tiempo = then1.time + then1.time
    #     return(tiempo)
    
    #     #return obj.salida - obj.ingreso

admin.site.site_header = 'Municipio de Loja 2020' 
admin.site.register(empresas, empresasAdmin)
admin.site.register(direcciones, direccionesAdmin)
admin.site.register(pozos, pozosAdmin)
admin.site.register(bitacora, bitacoraAdmin)

#admin.site.unregister(Group)