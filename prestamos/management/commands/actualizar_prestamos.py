from django.core.management.base import BaseCommand
from prestamos.models import Prestamo
from datetime import date


class Command(BaseCommand):
    help = 'Actualiza el estado de los préstamos retrasados automáticamente'

    def handle(self, *args, **options):
        # Buscar préstamos activos sin devolver
        prestamos_activos = Prestamo.objects.filter(
            estado__in=['prestado', 'retrasado'],
            fecha_real_devolucion__isnull=True
        )
        
        actualizados = 0
        retrasados_detectados = 0
        
        for prestamo in prestamos_activos:
            estado_anterior = prestamo.estado
            prestamo.actualizar_estado()
            
            if estado_anterior != prestamo.estado:
                actualizados += 1
                if prestamo.estado == 'retrasado':
                    retrasados_detectados += 1
                    self.stdout.write(
                        self.style.WARNING(
                            f'Préstamo {prestamo.codigo} retrasado: '
                            f'{prestamo.dias_retraso()} día(s) - '
                            f'Material: {prestamo.material.nombre}'
                        )
                    )
        
        if actualizados > 0:
            self.stdout.write(
                self.style.SUCCESS(
                    f'\n{actualizados} préstamo(s) actualizado(s)'
                )
            )
            if retrasados_detectados > 0:
                self.stdout.write(
                    self.style.WARNING(
                        f'{retrasados_detectados} préstamo(s) retrasado(s) detectado(s)'
                    )
                )
        else:
            self.stdout.write(
                self.style.SUCCESS('Todos los préstamos están al día')
            )

