from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from .views import CableadoDispersionView, HomeView
from .import views

app_name = "ducteria_app"


urlpatterns = [
    path(
        'dispersion/',
        views.CableadoDispersionView.as_view(),
        name="Dispersion_list"
    ),
    path(
        'home/',
        views.HomeView.as_view(),
        name='home'
    ),
    path(
        'login1/',
        views.Login1.as_view(),
        name='login1'
    )
]
