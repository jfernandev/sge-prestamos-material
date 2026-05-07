from rest_framework import viewsets
from .models import Material
from .serializers import MaterialSerializer


class MaterialViewSet(viewsets.ModelViewSet):
    """
    ViewSet para CRUD completo de Material.
    Endpoints:
    - GET /api/materiales/ (listar)
    - POST /api/materiales/ (crear)
    - GET /api/materiales/{id}/ (detalle)
    - PUT /api/materiales/{id}/ (actualizar completo)
    - PATCH /api/materiales/{id}/ (actualizar parcial)
    - DELETE /api/materiales/{id}/ (borrar)
    """
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
