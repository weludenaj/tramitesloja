from django.contrib import admin

from django.contrib.auth.models import Group, User
from datetime import datetime, date, time, timedelta

# Register your models here.
from .models import (
    seriedocumental, registropasivo
)

class seriedocumentalAdmin(admin.ModelAdmin):
    list_display = ("seriedocu",)
    search_fields = ("seriedocu",)
    

class registropasivoAdmin(admin.ModelAdmin):
    list_display = ("seccion", "seriedocu","subseccion", "subserie", "nrocaja", "expediente", "descripcion", "apertura", "cierre", "nrofojas", "destinofinal", "soporte", "zona", "estanteria", "bandeja", "observacion")
    search_fields = ("seccion", "subseccion", "subserie", "nrocaja", "expediente", "descripcion", "observacion")
    list_filter=("seccion","seriedocu","subseccion", "subserie", "estanteria")
    date_hierarchy="apertura"

 
admin.site.register(registropasivo, registropasivoAdmin)
admin.site.register(seriedocumental, seriedocumentalAdmin)