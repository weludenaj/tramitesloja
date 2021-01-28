from django.shortcuts import render

from django.views import generic

# Create your views here.

from django .contrib.auth.mixins import LoginRequiredMixin

from .models import bitacora


class BitacoraView(LoginRequiredMixin, generic.ListView):
    model = bitacora
    template_name = "bitacora/bitacora_list.html"
    context_object_name = 'obj'
    login_url = 'templates:home'