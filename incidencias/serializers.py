from rest_framework import serializers
from .models import Incidencia
from prestamos.serializers import PrestamoSerializer


class IncidenciaSerializer(serializers.ModelSerializer):
    prestamo_detalle = PrestamoSerializer(source='prestamo', read_only=True)
    
    class Meta:
        model = Incidencia
        fields = '__all__'


class IncidenciaCreateSerializer(serializers.ModelSerializer):
    """Serializer simplificado para crear incidencias"""
    class Meta:
        model = Incidencia
        fields = '__all__'

