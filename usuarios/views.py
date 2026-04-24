from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Usuario

class UsuarioListView(ListView):
    model = Usuario
    template_name = 'usuarios/usuario_list.html'

class UsuarioDetailView(DetailView):
    model = Usuario
    template_name = 'usuarios/usuario_detail.html'

class UsuarioCreateView(CreateView):
    model = Usuario
    fields = ['dni', 'nombre', 'apellidos', 'email', 'telefono', 'tipo_usuario']
    template_name = 'usuarios/usuario_form.html'
    success_url = reverse_lazy('usuario_list')

class UsuarioUpdateView(UpdateView):
    model = Usuario
    fields = ['dni', 'nombre', 'apellidos', 'email', 'telefono', 'tipo_usuario']
    template_name = 'usuarios/usuario_form.html'
    success_url = reverse_lazy('usuario_list')

class UsuarioDeleteView(DeleteView):
    model = Usuario
    template_name = 'usuarios/usuario_confirm_delete.html'
    success_url = reverse_lazy('usuario_list')
