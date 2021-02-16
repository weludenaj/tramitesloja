from django.shortcuts import render
from django.db.models import Q
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)
# models local

from .models import rexternos
from ckeditor.fields import RichTextField
from .forms import RegistroForm


class ListExternos(ListView):

    context_object_name = 'lista_externos'
    template_name = 'externos/lista.html'
    paginate_by = 50

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        # fecha1
        f1 = self.request.GET.get("fecha1", '')
        # fecha2
        f2 = self.request.GET.get("fecha2", '')

        if f1 and f2:
            return rexternos.objects.buscar_externos3(palabra_clave, f1, f2)
        else:
            return rexternos.objects.buscar_externos2(palabra_clave)
        # return rexternos.objects.buscar_externos2(palabra_clave, f1, f2)


class InicioView(LoginRequiredMixin, TemplateView):
    """ Vista que carga la pagina de inicio """
    template_name = 'home.html'
    #template_name = 'base/base.html'
    login_url = '/admin'


class addregister(CreateView):
    """ vista para registrar nuevo registro """
    template_name = 'externos/addregister.html'
    model = rexternos
    form_class = RegistroForm
    #fields = ['fechaingreso','guianro', 'usuario', 'descripcion', 'oficio', 'fechaentrega', 'enviadoa', 'observacion']
    #fields = ('__all__')
    success_url = '/'
    # reverse_lazy('persona_app:correcto')
    # persona_app es el nombre que se le pone en en la ruta y correcto es el name de la ruta
    # en las urls.py se app_name = "persona_app" eso nos indica todas las rutas
    # path('success/', views.SuccessView.as_view()), name= 'correcto')
    # reverse_lazy nos permite redireccionar. y mas cosas

    # def form_valid(self, form):
    #    registro = form.save()
    ## registro = form.save(commit=false)
    ##registro.fullname = registro.name + ' ' + registro.lastname
    # registro.save() esto actualiza la informacion
    #    return super(addregister, self).form_valid(form)


class SuccessView(TemplateView):
    template_name = "success.html"


class borrarregistro(DeleteView):
    template_name = "borrado.html"
    model = rexternos
    success_url = reverse_lazy('externos_app:correcto')


class rexternosupdate(UpdateView):
    template_name = "actualiza.html"
    model = rexternos
    fields = [
        'fechaingreso',
        'guianro',
        'usuario',
        'descripcion',
        'oficio',
        'fechaentrega',
        'enviadoa',
        'observacion',
        'atendido',
        'documentos',
    ]
    # fields = ('__all__')
    success_url = reverse_lazy('externos_app:listadoexterno')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print('++++++++++Valida++++++++++++++++++++')
        print(request.POST)
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        print('++++++++++Valida funcions ++++++++++++++++++++')
        return super(rexternosupdate, self).form_valid(form)


class rexternosListView(ListView):
    #model = registroarchivos
    template_name = "lista.html"
    context_object_name = 'listaNumeros'
    paginate_by = 10
    ordering = 'fechaingreso'

    #queryset = ['0', '10', '30', '50']

    def get_queryset(self):    # Escribo el codigo
        usuarios = self.request.GET.get("nombre", '')
        listaNumeros = rexternos.objects.filter(
            Q(usuario__icontains=usuarios) | Q(guianro__icontains=usuarios))
        return listaNumeros
