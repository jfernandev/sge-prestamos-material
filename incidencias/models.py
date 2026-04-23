from django.db import models
from prestamos.models import Prestamo

class Incidencia(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    fecha = models.DateField()
    descripcion = models.TextField()
    tipo_incidencia = models.CharField(max_length=30, choices=[('daño', 'Daño'), ('pérdida', 'Pérdida'), ('otro', 'Otro')], default='daño')
    prestamo = models.ForeignKey(Prestamo, on_delete=models.CASCADE, related_name='incidencias')

    def __str__(self):
        return f"Incidencia {self.codigo} - {self.tipo_incidencia}"
