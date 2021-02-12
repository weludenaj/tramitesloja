from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

app_name = "externos_app"

urlpatterns = [
    path(
        '',
        views.InicioView.as_view(),
        name='inicio'
    ),
    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='base/login.html'
        ),
        name='login'
    ),
    path(
        'externos/',
        views.ListExternos.as_view(),
        name="externos"
    ),
    path(
        'listaexternos/',
        views.rexternosListView.as_view(),
        name="listadoexterno"
    ),
    path(
        'insertarexterno/',
        views.addregister.as_view(),
        name="insertar"
    ),
    path(
        'actualizar/<pk>/',
        views.rexternosupdate.as_view(),
        name='modificar_registro'
    ),
    path(
        'borrar/<pk>/',
        views.borrarregistro.as_view(),
        name='borrar_registro'
    ),
    path(
        'success/',
        views.SuccessView.as_view(),
        name='correcto'
    ),

]
