from django.db import models
from django.core.exceptions import ValidationError
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
        """Validar que el material no esté ya prestado"""
        super().clean()
        if self.material and not self.pk:  # Solo al crear
            prestamos_activos = Prestamo.objects.filter(
                material=self.material,
                estado__in=['prestado', 'retrasado']
            )
            if prestamos_activos.exists():
                raise ValidationError({
                    'material': f'El material "{self.material.nombre}" ya está prestado.'
                })
    
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
    
    def actualizar_estado(self):
        """Actualiza el estado del préstamo y material (sin recursión)"""
        if self.fecha_real_devolucion:
            nuevo_estado = 'devuelto'
            estado_material = 'disponible'
        elif self.esta_retrasado():
            nuevo_estado = 'retrasado'
            estado_material = 'retrasado'
        else:
            nuevo_estado = 'prestado'
            estado_material = 'prestado'
        
        # Actualizar solo si cambió
        if self.estado != nuevo_estado:
            Prestamo.objects.filter(pk=self.pk).update(estado=nuevo_estado)
            self.estado = nuevo_estado
        
        if self.material.estado != estado_material:
            Material.objects.filter(pk=self.material.pk).update(estado=estado_material)
            self.material.estado = estado_material
    
    def save(self, *args, **kwargs):
        is_new = self.pk is None
        if is_new:
            self.full_clean()
        super().save(*args, **kwargs)
        if is_new and self.material:
            Material.objects.filter(pk=self.material.pk).update(estado='prestado')

