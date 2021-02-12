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

from .models import bitacora, direcciones, pozos

from .managers import pozosManager


class BitacoraView(LoginRequiredMixin, generic.ListView):
    model = bitacora
    template_name = "bitacora/bitacora_list.html"
    context_object_name = 'obj'
    login_url = 'templates:home'


class ListaPozosView(ListView):
    """Lista de Pozos """
    template_name = 'bitacora/listapozos.html'
    context_object_name = 'lista_pozos'
    paginate_by = 8

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')

        return pozos.objects.buscar_pozos(palabra_clave)


class ListSwitches(ListView):
    context_object_name = 'lista_switches'
    template_name = 'inventario/listaswitches.html'
    paginate_by = 8

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')

        return Switches.objects.buscar_switches(palabra_clave)


class ListByDireccionPozoView(ListView):
    """Lista de Pozos por direccion"""
    template_name = 'bitacora/listapozosxdir.html'
    context_object_name = 'lista_pozos'
    paginate_by = 8

    def get_queryset(self):
        direccionv = self.kwargs['direccion']

        lista = pozos.objects.filter(
            direccion__id=direccionv
        ).order_by('numero')

        return lista


class ListaPozosDirView(ListView):
    """Lista de Pozos por direccion"""
    model = direcciones
    template_name = 'bitacora/listadireccion.html'
    context_object_name = 'lista_direcciones'
    paginate_by = 8


# def get_queryset(self):
#     """
#     Return the list of items for this view.
#     The return value must be an iterable and may be an instance of
#     `QuerySet` in which case `QuerySet` specific behavior will be enabled.
#     """
#     if self.queryset is not None:
#         queryset = self.queryset
#         if isinstance(queryset, QuerySet):
#             queryset = queryset.all()
#     elif self.model is not None:
#         queryset = self.model._default_manager.all()
#     else:
#         raise ImproperlyConfigured(
#             "%(cls)s is missing a QuerySet. Define "
#             "%(cls)s.model, %(cls)s.queryset, or override "
#             "%(cls)s.get_queryset()." % {
#                 'cls': self.__class__.__name__
#             }
#         )
#     ordering = self.get_ordering()
#     if ordering:
#         if isinstance(ordering, str):
#             ordering = (ordering,)
#         queryset = queryset.order_by(*ordering)
#     return queryset

class pozosupdate(UpdateView):
    template_name = "bitacora/actualizar_pozo.html"
    model = pozos
    fields = [
        'numero',
        'direccion',
        'posicion',
        'tipos',
        'observacion',
    ]
    # fields = ('__all__')
    success_url = reverse_lazy('bitacora_app:pozos_lista')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print('++++++++++Valida++++++++++++++++++++')
        print(request.POST)
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        print('++++++++++Valida funcions ++++++++++++++++++++')
        return super(pozosupdate, self).form_valid(form)
