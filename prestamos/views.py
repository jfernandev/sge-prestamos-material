from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from .models import Prestamo
from .serializers import PrestamoSerializer, PrestamoCreateSerializer


class PrestamoViewSet(viewsets.ModelViewSet):
    """
    ViewSet para CRUD completo de Prestamo.
    Incluye acción personalizada para cerrar préstamos.
    """
    queryset = Prestamo.objects.all()
    
    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return PrestamoCreateSerializer
        return PrestamoSerializer
    
    @action(detail=True, methods=['post'])
    def cerrar(self, request, pk=None):
        """
        Acción personalizada para cerrar un préstamo.
        POST /api/prestamos/{id}/cerrar/
        """
        prestamo = self.get_object()
        prestamo.fecha_real_devolucion = timezone.now().date()
        prestamo.estado = 'devuelto'
        prestamo.save()
        serializer = self.get_serializer(prestamo)
        return Response(serializer.data)
