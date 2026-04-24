from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.utils import timezone
from .models import Prestamo

class PrestamoListView(ListView):
    model = Prestamo
    template_name = 'prestamos/prestamo_list.html'

class PrestamoDetailView(DetailView):
    model = Prestamo
    template_name = 'prestamos/prestamo_detail.html'

class PrestamoCreateView(CreateView):
    model = Prestamo
    fields = ['codigo', 'fecha_prestamo', 'fecha_prevista_devolucion', 'usuario', 'material', 'observaciones']
    template_name = 'prestamos/prestamo_form.html'
    success_url = reverse_lazy('prestamo_list')

class PrestamoUpdateView(UpdateView):
    model = Prestamo
    fields = ['codigo', 'fecha_prestamo', 'fecha_prevista_devolucion', 'fecha_real_devolucion', 'estado', 'usuario', 'material', 'observaciones']
    template_name = 'prestamos/prestamo_form.html'
    success_url = reverse_lazy('prestamo_list')

class PrestamoCerrarView(View):
    def get(self, request, pk):
        prestamo = get_object_or_404(Prestamo, pk=pk)
        return render(request, 'prestamos/prestamo_cerrar.html', {'prestamo': prestamo})
    
    def post(self, request, pk):
        prestamo = get_object_or_404(Prestamo, pk=pk)
        prestamo.fecha_real_devolucion = timezone.now().date()
        prestamo.estado = 'devuelto'
        prestamo.save()
        return redirect('prestamo_list')

class PrestamoDeleteView(DeleteView):
    model = Prestamo
    template_name = 'prestamos/prestamo_confirm_delete.html'
    success_url = reverse_lazy('prestamo_list')
