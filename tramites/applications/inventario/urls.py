from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

# app_name = "inventario_app"

urlpatterns = [
    path(
        'listaips/',
        views.ListIps.as_view(),
        name="Ips"
    ),
    path(
        'listaempleado/',
        views.ListEmpleados.as_view(),
        name="Empleados"
    ),
    path(
        'listaswitch/',
        views.ListSwitches.as_view(),
        name="Switches"
    ),
    path(
        'addswitch/',
        views.CrearSwitch.as_view(),
        name="AddSwitch"
    ),
    path(
        'adddireccion/',
        views.DireccionesNew.as_view(),
        name="AddDireccion"
    ),
    path(
        'actualizarip/<pk>/',
        views.IpUpdate.as_view(),
        name='modificar_ip'
    ),
    path(
        'actualizarempleado/<pk>/',
        views.EmpleadoUpdate.as_view(),
        name='modificar_empleado'
    ),
    path(
        'actualizarempleado2/<pk>/',
        views.EmpleadoUpdate2.as_view(),
        name='modificar_empleado2'
    ),
    path(
        'actualizarswitch/<pk>/',
        views.ActualizarSwitch.as_view(),
        name='modificar_switch'
    ),
    path(
        'lista_by_switch/<nombre>/',
        views.ListBySwitchIp.as_view(),
        name='ip_switch'
    ),
]
