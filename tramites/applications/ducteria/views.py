from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

from django.views import generic

from django.db.models import Q

from django.urls import reverse_lazy

import datetime

from django.http import HttpResponse

# Create your views here.
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)

from django .contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.decorators import login_required, permission_required

from applications.bitacora.models import empresas, direcciones, pozos
from .models import CableadoDispersion, Dispersion
from .forms import CableadoDispersionForm

#from .managers import pozosManager


class Login1(LoginRequiredMixin, TemplateView):
    template_name = 'base/login1.html'
    login_url = '/login'


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'base/base.html'
    login_url = '/login1'


class CableadoDispersionView(ListView):
    model = CableadoDispersion
    """Lista de Cables Dispersion """
    template_name = 'ducteria/listadispersion.html'
    context_object_name = 'lista_dispersion'
    paginate_by = 8

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')

        return CableadoDispersion.objects.buscar(palabra_clave)


@login_required(login_url='/login/')
def RegistroDispersion(request, empresa_id=None):
    template_name = "ducteria/registrodispersion.html"
    dispersion = CableadoDispersion.objects.filter(empresa=empresa_id)
    form_dispersion = {}
    contexto = {}

    if request.method == 'GET':
        form_dispersion = CableadoDispersionForm()
        dispersion = Dispersion.objects.filter(
            pk=Dispersion).first()

        if dispersion:
            detalle = Dispersion.objects.filter(CableadoDispersion=dispersion)


class CableDispersionUpdate(UpdateView):
    template_name = "ducteria/actualizar_dispersion.html"
    model = CableadoDispersion
    fields = ['__all__']
    # fields = ('__all__')
    success_url = reverse_lazy('ducteria_app:CablesDispersion')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print('++++++++++Valida++++++++++++++++++++')
        print(request.POST)
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        print('++++++++++Valida funcions ++++++++++++++++++++')
        return super(CableDispersionUpdate, self).form_valid(form)
