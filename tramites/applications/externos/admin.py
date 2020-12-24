from django.contrib import admin

# Register your models here.

from django.contrib.auth.models import Group, User


# Register your models here.
from .models import (
    rexternos,
    Administrador,
    contraloria,
    tramitesdigitales,
    Ciudad, 
    Oficioindice, 
    Dependencias, 
    SecretariaG, 
    resoluciones,
    ordenanzas,
    MemorandoAlcaldia,
    EntidadExterna,
    Comunicaciones,
    planificacion,
    convenios,
)
from applications.internos.models import Dependencia, rinternos 


class rexternosAdmin(admin.ModelAdmin):
    list_display=("fechaingreso","guianro","usuario","descripcion","oficio","fechaentrega","enviadoa","observacion")
    search_fields=("fechaingreso", "guianro", "usuario", "oficio", "descripcion") 
    #list_filter=("fechaingreso",)
    date_hierarchy="fechaingreso"   

class rinternosAdmin(admin.ModelAdmin):
     list_display=("secuencia","fechaingreso","guianro","remite","descripcion","nrotramite","fechadespacho","enviadoa","observacion")
     search_fields=("secuencia","fechaingreso", "guianro", "remite")
    # list_filter=("fechaingreso",)
     date_hierarchy="fechaingreso"

class DependenciaAdmin(admin.ModelAdmin):
    list_display=("nombre",)
    search_fields=("nombre",)

class AdministradorAdmin(admin.ModelAdmin):
    list_display=("numerocontrato","administrador", "nombredelcontrato","contratista","fechainicio", "fechafinal", "memosend", "memoreceived")
    search_fields=("administrador", "nombredelcontrato", "contratista","memosend", "memoreceived")
    ordering = ("-numerocontrato", "administrador", "fechainicio", "fechafinal") 
    #list_filter=("fechaingreso",)
    date_hierarchy="fechainicio"
    
class contraloriaAdmin(admin.ModelAdmin):
    list_display=("secuencia","fechaingreso","memorando","recomendacion", "dependencia", "funcionario", "contestacion", "seguimiento", "fechalastupdate", "observacion", "concluido", "documentos")
    search_fields=("fechaingreso", "memorando", "recomendacion", "dependencia", "funcionario", "contestacion")
    date_hierarchy="fechaingreso"

class tramitesdigitalesAdmin(admin.ModelAdmin):
    list_display=("fechaingreso","registrado","identificacion","correo", "usuario", "tramite", "ceropapeles", "enviadoa", "estado", "observacion")
    search_fields=("fechaingreso", "registrado", "identificacion", "correo", "usuario", "ceropapeles")
    date_hierarchy="fechaingreso"

# class oficiosenviadosAdmin(admin.ModelAdmin):
#     list_display=("numoficio","institucion", "destinatario", "asunto", "detalle", "fecha", "anexos")
#     search_fields=("numoficio","institucion", "destinatario", "asunto", "detalle")
#     date_hierarchy="fecha"

class DependenciasAdmin(admin.ModelAdmin):
    list_display=("nombre",)
    search_fields=("nombre",)
    ordering = ("nombre",)

class OficioindiceAdmin(admin.ModelAdmin):
    list_display=("numoficio", "origen", "fecha",  "destinatario", "dpto", "destino", "observacion", "detalle")
    search_fields=("numoficio", "destinatario", "dpto", "observacion")
    date_hierarchy="fecha"
    ordering = ("-id",)	

class SecretariaGAdmin(admin.ModelAdmin):
    list_display=("fecha","tramite","remite", "detalle", "sumilla", "observacion")
    search_fields=("fecha","tramite", "remite", "detalle", "sumilla")
    date_hierarchy="fecha"
    ordering = ("-id",)	

class resolucionesAdmin(admin.ModelAdmin):
    list_display=("resolucion", "fecha", "detalle", "observacion")
    search_fields=("resolucion", "detalle")
    date_hierarchy=("fecha")
    ordering =("fecha",)

class MemorandoAlcaldiaAdmin(admin.ModelAdmin):
    list_display=("nummemorando", "fecha", "dirigidoa", "dependencia", "asunto", "contenido", "observacion")
    search_fields=("nummemorando", "dirigidoa", "asunto", "contenido", "observacion")
    date_hierarchy=("fecha")
    ordering =("-nummemorando",)

class ordenanzasAdmin(admin.ModelAdmin):
    list_display=("numero", "ordenanza", "suscrita", "primerdebate", "segundodebate", "sancionada", "observacion", "registro")
    search_fields=("numero", "ordenanza", "suscrita","observaciones", "registro",)
    date_hierarchy=("suscrita")
    ordering =("-id",)

class EntidadExternaAdmin(admin.ModelAdmin):
    list_display=("id", "Entidad")
    search_fields=("Entidad",)
    ordering=("Entidad",)

class ComunicacionesAdmin(admin.ModelAdmin):
    list_display=("numero","medio", "entidad","remite", "asunto","contestado","observacion" )
    search_fields=("medio","remite","asunto","contestado",)
    ordering=("-fecha",)

class planificacionAdmin(admin.ModelAdmin):
    list_display=("registro", "fecha", "guianro","categoria","referencia", "asunto","remitente","departamento","destinatario","departamentof","observacion")
    search_fields=("registro", "fecha", "guianro","categoria","referencia", "asunto","remitente","departamento","destinatario","departamentof","observacion")
    ordering=("-fecha",)


class conveniosAdmin(admin.ModelAdmin):
    list_display=("registro","institucion","convenio","objeto","plazo","fechainicio","fechafinal","cumplimiento","encargado","dependencia","observacion")
    search_fields=("registro","institucion","convenio","objeto","plazo","fechainicio","fechafinal","cumplimiento","encargado","dependencia","observacion")
    ordering=("-fechainicio",)

admin.site.site_header = 'Municipio de Loja 2020' 
admin.site.register(rexternos, rexternosAdmin)
admin.site.register(rinternos,rinternosAdmin)
admin.site.register(Dependencia,DependenciaAdmin)
admin.site.register(Administrador, AdministradorAdmin)
admin.site.register(contraloria, contraloriaAdmin)
admin.site.register(tramitesdigitales, tramitesdigitalesAdmin)
admin.site.register(Dependencias, DependenciasAdmin)
admin.site.register(Oficioindice, OficioindiceAdmin)
admin.site.register(Ciudad)
admin.site.register(SecretariaG, SecretariaGAdmin)
admin.site.register(resoluciones, resolucionesAdmin)
admin.site.register(ordenanzas, ordenanzasAdmin)
admin.site.register(MemorandoAlcaldia, MemorandoAlcaldiaAdmin)
admin.site.register(EntidadExterna, EntidadExternaAdmin)
admin.site.register(Comunicaciones,ComunicacionesAdmin)
admin.site.register(planificacion,planificacionAdmin)
admin.site.register(convenios,conveniosAdmin)
admin.site.unregister(Group)
#admin.site.unregister(User)
