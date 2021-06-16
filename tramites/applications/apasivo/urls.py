from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from .views import PasivoView
from . import views

app_name = "pasivo_app"

urlpatterns = [
    path(
        'apasivo/',
        views.PasivoView.as_view(),
        name="pasivo_list"
    ),
]