from typing import List
from django.shortcuts import render


# Create your views here.

from django.views.generic import ListView, CreateView, UpdateView

from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib import messages

from .models import Direcciones, Empleados, Switches

from .forms import DireccionesForm


class ListIps(LoginRequiredMixin, ListView):
    context_object_name = 'lista_ips'
    template_name = 'inventario/listaips.html'
    login_url = '/admin'
    paginate_by = 6

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')

        return Direcciones.objects.buscar_ip1(palabra_clave)


class ListIpsEmpleado(ListView):
    context_object_name = 'lista_ips_empleado'
    template_name = 'inventario/listaipsempleado.html'
    paginate_by = 6

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')

        return Direcciones.objects.listar_ips_empleado(palabra_clave)


class DireccionesNew(LoginRequiredMixin, CreateView):
    model = Direcciones
    template_name = 'inventario/adddireccion.html'
    context_object_name = 'obj'
    form_class = DireccionesForm
    success_url = reverse_lazy('inventario_app:Ips')
    login_url = '/admin'

    def form_valid(self, form):
        form.instance.uc = self.request.user
        messages.success(
            self.request, f'Has creado correctamente la direccion {Direcciones.direccion}')
        return super().form_valid(form)


class ListEmpleados(ListView):
    context_object_name = 'lista_empleados'
    template_name = 'inventario/listaempleados1.html'
    paginate_by = 8

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')

        return Empleados.objects.buscar_empleados(palabra_clave)


class ListSwitches(ListView):
    context_object_name = 'lista_switches'
    template_name = 'inventario/listaswitches.html'
    paginate_by = 8

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')

        return Switches.objects.buscar_switches(palabra_clave)


class CrearSwitch(CreateView):
    template_name = "inventario/addswitch.html"
    model = Switches
    fields = ['nombre', 'puertos', 'rack',
              'marca', 'modelo', 'serial', 'ip', 'mac']
    success_url = 'inventario_app:switches'


class IpUpdate(UpdateView):
    template_name = "inventario/actualizar_modal.html"
    model = Direcciones
    fields = [
        'direccion',
        'tipos',
        'categoria',
        'macaddress',
        'equipo',
        'switch',
        'puerto',
        'dependencia',
        'empleado',
        'observacion',
    ]
    # fields = ('__all__')
    success_url = reverse_lazy('inventario_app:Ips')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print('++++++++++Valida++++++++++++++++++++')
        print(request.POST)
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        print('++++++++++Valida funcions ++++++++++++++++++++')
        return super(IpUpdate, self).form_valid(form)


class EmpleadoUpdate(UpdateView):
    template_name = "inventario/actualizar_empleado.html"
    model = Empleados
    fields = [
        'cedula',
        'nombres',
        'correo',
        'extension',
        'celular',
        'cargo',
        'id',
    ]
    # fields = ('__all__')
    success_url = reverse_lazy('inventario_app:Empleados')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print('++++++++++Valida++++++++++++++++++++')
        print(request.POST)
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        print('++++++++++Valida funcions ++++++++++++++++++++')
        return super(EmpleadoUpdate, self).form_valid(form)


class EmpleadoUpdate2(UpdateView):
    template_name = "inventario/actualizar_empleadomodal.html"
    model = Empleados
    fields = [
        'cedula',
        'nombres',
        'correo',
        'extension',
        'celular',
        'cargo',
        'id',
    ]
    # fields = ('__all__')
    success_url = reverse_lazy('inventario_app:Empleados')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print('++++++++++Valida++++++++++++++++++++')
        print(request.POST)
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        print('++++++++++Valida funcions ++++++++++++++++++++')
        return super(EmpleadoUpdate2, self).form_valid(form)


class SwitchesListView(ListView):
    model = Switches
    template_name = "inventario/listaswitches.html"


class ActualizarSwitch(UpdateView):
    template_name = "inventario/actualizar_switch.html"
    model = Switches

    fields = [
        'nombre',
        'puertos',
        'rack',
        'marca',
        'modelo',
        'serial',
        'ip',
        'mac',
    ]
    # fields = ('__all__')
    success_url = reverse_lazy('Switches')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print('++++++++++Valida++++++++++++++++++++')
        print(request.POST)
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        print('++++++++++Valida funcions ++++++++++++++++++++')
        return super(ActualizarSwitch, self).form_valid(form)


class ListBySwitchIp(ListView):
    """Lista de Ips por Switch"""
    template_name = 'inventario/list_by_swith.html'
    context_object_name = 'lista_switches'
    paginate_by = 8

    def get_queryset(self):
        switch = self.kwargs['nombre']
        lista = Direcciones.objects.filter(
            switch__nombre=switch
        )
        return lista
