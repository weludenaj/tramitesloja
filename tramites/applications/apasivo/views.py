from django.shortcuts import render

from django.views import generic

from django.db.models import Q

from django.urls import reverse_lazy

# Create your views here.
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)

from django .contrib.auth.mixins import LoginRequiredMixin

from .models import registropasivo

# # from .managers import pozosManager


class PasivoView(LoginRequiredMixin, generic.ListView):
    model = registropasivo
    template_name = "apasivo/apasivo_list.html"
    context_object_name = 'obj'
    login_url = 'templates:home'
