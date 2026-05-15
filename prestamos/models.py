from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import date
from materiales.models import Material
from usuarios.models import Usuario

class Prestamo(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    fecha_prestamo = models.DateField()
    fecha_prevista_devolucion = models.DateField()
    fecha_real_devolucion = models.DateField(null=True, blank=True)
    estado = models.CharField(max_length=20, choices=[
        ('prestado', 'Prestado'), 
        ('devuelto', 'Devuelto'), 
        ('retrasado', 'Retrasado')
    ], default='prestado')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='prestamos')
    material = models.ForeignKey(Material, on_delete=models.CASCADE, related_name='prestamos')
    observaciones = models.TextField(blank=True)

    def __str__(self):
        return f"Préstamo {self.codigo} - {self.material.nombre} a {self.usuario.nombre}"
    
    def clean(self):
        """Validaciones personalizadas"""
        super().clean()
        
        # Validar que el material no esté ya prestado
        if self.material:
            prestamos_activos = Prestamo.objects.filter(
                material=self.material,
                estado__in=['prestado', 'retrasado']
            ).exclude(pk=self.pk if self.pk else None)
            
            if prestamos_activos.exists():
                raise ValidationError({
                    'material': f'El material "{self.material.nombre}" ya está prestado actualmente.'
                })
    
    def actualizar_estado(self):
        """Actualiza el estado del préstamo según las fechas"""
        if self.fecha_real_devolucion:
            # Si ya fue devuelto
            self.estado = 'devuelto'
            self.material.estado = 'disponible'
            self.material.save()
        elif date.today() > self.fecha_prevista_devolucion:
            # Si está retrasado
            self.estado = 'retrasado'
            self.material.estado = 'retrasado'
            self.material.save()
        else:
            # Si está activo
            self.estado = 'prestado'
            self.material.estado = 'prestado'
            self.material.save()
        
        self.save()
    
    def esta_retrasado(self):
        """Verifica si el préstamo está retrasado"""
        if self.fecha_real_devolucion:
            return False
        return date.today() > self.fecha_prevista_devolucion
    
    def dias_retraso(self):
        """Calcula los días de retraso"""
        if not self.esta_retrasado():
            return 0
        return (date.today() - self.fecha_prevista_devolucion).days
    
    def save(self, *args, **kwargs):
        """Override save para actualizar estados automáticamente"""
        # Al crear un préstamo nuevo
        is_new = self.pk is None
        
        if is_new:
            # Validar que el material esté disponible
            self.full_clean()
            # Actualizar estado del material a prestado
            self.material.estado = 'prestado'
            self.material.save()
        
        super().save(*args, **kwargs)
        
        # Después de guardar, actualizar estado si es necesario
        if not is_new:
            self.actualizar_estado()
