from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Incidencia

class IncidenciaListView(ListView):
    model = Incidencia
    template_name = 'incidencias/incidencia_list.html'

class IncidenciaDetailView(DetailView):
    model = Incidencia
    template_name = 'incidencias/incidencia_detail.html'

class IncidenciaCreateView(CreateView):
    model = Incidencia
    fields = ['codigo', 'fecha', 'descripcion', 'tipo_incidencia', 'prestamo']
    template_name = 'incidencias/incidencia_form.html'
    success_url = reverse_lazy('incidencia_list')

class IncidenciaUpdateView(UpdateView):
    model = Incidencia
    fields = ['codigo', 'fecha', 'descripcion', 'tipo_incidencia', 'prestamo']
    template_name = 'incidencias/incidencia_form.html'
    success_url = reverse_lazy('incidencia_list')

class IncidenciaDeleteView(DeleteView):
    model = Incidencia
    template_name = 'incidencias/incidencia_confirm_delete.html'
    success_url = reverse_lazy('incidencia_list')
