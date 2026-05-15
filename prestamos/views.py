from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from django.core.exceptions import ValidationError as DjangoValidationError
from .models import Prestamo
from .serializers import PrestamoSerializer, PrestamoCreateSerializer


class PrestamoViewSet(viewsets.ModelViewSet):
    """
    ViewSet para CRUD completo de Prestamo.
    Incluye acción personalizada para cerrar préstamos y validaciones de negocio.
    """
    queryset = Prestamo.objects.all()
    
    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return PrestamoCreateSerializer
        return PrestamoSerializer
    
    def perform_create(self, serializer):
        """Override para validar antes de crear"""
        try:
            instance = serializer.save()
            # El método save() del modelo ya actualiza el estado del material
        except DjangoValidationError as e:
            # Convertir errores de validación Django a formato DRF
            from rest_framework.exceptions import ValidationError
            raise ValidationError(e.message_dict)
    
    def perform_update(self, serializer):
        """Override para actualizar estado después de editar"""
        instance = serializer.save()
        instance.actualizar_estado()
    
    @action(detail=True, methods=['post'])
    def cerrar(self, request, pk=None):
        """
        Acción personalizada para cerrar un préstamo (devolución).
        POST /api/prestamos/{id}/cerrar/
        Actualiza automáticamente el estado del material a 'disponible'
        """
        prestamo = self.get_object()
        prestamo.fecha_real_devolucion = timezone.now().date()
        prestamo.actualizar_estado()  # Esto actualiza tanto préstamo como material
        serializer = self.get_serializer(prestamo)
        return Response(serializer.data)
