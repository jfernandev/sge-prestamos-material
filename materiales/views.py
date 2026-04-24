from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Material

class MaterialListView(ListView):
    model = Material
    template_name = 'materiales/material_list.html'

class MaterialDetailView(DetailView):
    model = Material
    template_name = 'materiales/material_detail.html'

class MaterialCreateView(CreateView):
    model = Material
    fields = ['codigo', 'nombre', 'descripcion', 'categoria', 'estado', 'ubicacion']
    template_name = 'materiales/material_form.html'
    success_url = reverse_lazy('material_list')

class MaterialUpdateView(UpdateView):
    model = Material
    fields = ['codigo', 'nombre', 'descripcion', 'categoria', 'estado', 'ubicacion']
    template_name = 'materiales/material_form.html'
    success_url = reverse_lazy('material_list')

class MaterialDeleteView(DeleteView):
    model = Material
    template_name = 'materiales/material_confirm_delete.html'
    success_url = reverse_lazy('material_list')
