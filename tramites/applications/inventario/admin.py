from enum import unique
from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import Group, User
from datetime import datetime, date, time, timedelta

# Register your models here.
from .models import (
    Switches,
    TipoDireccion,
    Categorias,
    Direcciones,
    Empleados,
    Dependencias,
)

class SwitchesAdmin(admin.ModelAdmin):
    list_display=("nombre","puertos","rack")
    search_fields=("nombre", "rack") 
    #list_filter=("fechaingreso",)
    #date_hierarchy="fechaingreso" 

class TipoDireccionAdmin(admin.ModelAdmin):
    list_display=("tipo",)
    search_fields=("tipo",) 
    #list_filter=("fechaingreso",)
    #date_hierarchy="fechaingreso" 
    
class CategoriasAdmin(admin.ModelAdmin):
    list_display=("categoria",)
    search_fields=("categoria",)     
    
class DependenciasAdmin(admin.ModelAdmin):
    list_display=("dependencia",)
    search_fields=("dependencia",) 

class EmpleadosAdmin(admin.ModelAdmin):
    list_display=("nombres", "correo", "extension")
    search_fields=("nombres","cedula") 

    

class DireccionesAdmin(admin.ModelAdmin):
    list_display=("direccion", "tipos", "categoria", "macaddress","equipo", "switch", "dependencia", "empleado","observacion")
    search_fields=("direccion", "macaddress","equipo", "observacion") 
  
  
    
    
admin.site.site_header = 'Municipio de Loja 2021 - Direccion de Tecnologia' 
admin.site.register(Switches, SwitchesAdmin)
admin.site.register(Categorias, CategoriasAdmin)
admin.site.register(TipoDireccion, TipoDireccionAdmin)
admin.site.register(Empleados, EmpleadosAdmin)
admin.site.register(Dependencias, DependenciasAdmin)
admin.site.register(Direcciones,DireccionesAdmin)

