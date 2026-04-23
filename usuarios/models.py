from django.db import models

class Usuario(models.Model):
    dni = models.CharField(max_length=12, unique=True)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True)
    tipo_usuario = models.CharField(max_length=30, choices=[('estudiante', 'Estudiante'), ('empleado', 'Empleado'), ('departamento', 'Departamento')], default='estudiante')

    def __str__(self):
        return f"{self.nombre} {self.apellidos} ({self.dni})"
