from django.contrib import admin

from django.contrib.auth.models import Group, User
from datetime import datetime, date, time, timedelta

# Register your models here.
from .models import (
    registropasivo
)

class registropasivoAdmin(admin.ModelAdmin):
    list_display = ("seccion", "nrocaja", "expediente", "descripcion", "apertura", "cierre", "nrofojas", "destinofinal", "soporte", "zona", "estanteria", "bandeja", "observacion")
    search_fields = ("seccion", "nrocaja", "expediente", "descripcion", "apertura", "cierre", "nrofojas", "destinofinal", "soporte", "zona", "estanteria", "bandeja", "observacion")
    list_filter=("seccion",)
    # date_hierarchy="fechaingreso"

admin.site.register(registropasivo, registropasivoAdmin)