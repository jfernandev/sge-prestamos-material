from django.db import models

class Material(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    categoria = models.CharField(max_length=50)
    estado = models.CharField(max_length=20, choices=[('disponible', 'Disponible'), ('prestado', 'Prestado'), ('retrasado', 'Retrasado')], default='disponible')
    ubicacion = models.CharField(max_length=100, blank=True)
    fecha_alta = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} ({self.codigo})"
