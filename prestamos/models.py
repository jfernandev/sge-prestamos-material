from django.db import models
from materiales.models import Material
from usuarios.models import Usuario

class Prestamo(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    fecha_prestamo = models.DateField()
    fecha_prevista_devolucion = models.DateField()
    fecha_real_devolucion = models.DateField(null=True, blank=True)
    estado = models.CharField(max_length=20, choices=[('activo', 'Activo'), ('devuelto', 'Devuelto'), ('retrasado', 'Retrasado')], default='activo')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='prestamos')
    material = models.ForeignKey(Material, on_delete=models.CASCADE, related_name='prestamos')
    observaciones = models.TextField(blank=True)

    def __str__(self):
        return f"Préstamo {self.codigo} - {self.material.nombre} a {self.usuario.nombre}"
