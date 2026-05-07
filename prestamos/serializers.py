from rest_framework import serializers
from .models import Prestamo
from materiales.serializers import MaterialSerializer
from usuarios.serializers import UsuarioSerializer


class PrestamoSerializer(serializers.ModelSerializer):
    material_detalle = MaterialSerializer(source='material', read_only=True)
    usuario_detalle = UsuarioSerializer(source='usuario', read_only=True)
    
    class Meta:
        model = Prestamo
        fields = '__all__'


class PrestamoCreateSerializer(serializers.ModelSerializer):
    """Serializer simplificado para crear préstamos"""
    class Meta:
        model = Prestamo
        fields = '__all__'

