from rest_framework import viewsets
from .models import Incidencia
from .serializers import IncidenciaSerializer, IncidenciaCreateSerializer


class IncidenciaViewSet(viewsets.ModelViewSet):
    """
    ViewSet para CRUD completo de Incidencia.
    """
    queryset = Incidencia.objects.all()
    
    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return IncidenciaCreateSerializer
        return IncidenciaSerializer

