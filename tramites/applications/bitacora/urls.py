from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from .views import BitacoraView, ListByDireccionPozoView
from . import views

app_name = "bitacora_app"

urlpatterns = [
    path(
        'bitacora/',
        views.BitacoraView.as_view(),
        name="bitacora_list"
    ),
    path(
        'listapozo/<direccion>',
        views.ListByDireccionPozoView.as_view(),
        name="pozos_list"
    ),
    path(
        'listarpozos/',
        views.ListaPozosView.as_view(),
        name="pozos_lista"
    ),
    path(
        'listarpozosfil/',
        views.ListaPozosDirView.as_view(),
        name="pozos_lista2"
    ),
    path(
        'actualizarpozo/<pk>/',
        views.pozosupdate.as_view(),
        name='modificar_pozo'
    ),
]
