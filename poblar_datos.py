#!/usr/bin/env python
"""Script para poblar la base de datos con datos de prueba"""
import os
import django
from datetime import date, timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from materiales.models import Material
from usuarios.models import Usuario
from prestamos.models import Prestamo
from incidencias.models import Incidencia

print("🗑️  Limpiando datos existentes...")
Incidencia.objects.all().delete()
Prestamo.objects.all().delete()
Material.objects.all().delete()
Usuario.objects.all().delete()
print("✅ Datos limpiados\n")

# MATERIALES
print("📦 Creando materiales...")
materiales_data = [
    {"codigo": "LAP001", "nombre": "Laptop HP EliteBook", "categoria": "Informática", "estado": "disponible", "ubicacion": "Almacén A"},
    {"codigo": "LAP002", "nombre": "Laptop Dell Latitude", "categoria": "Informática", "estado": "disponible", "ubicacion": "Almacén A"},
    {"codigo": "LAP003", "nombre": "MacBook Air M2", "categoria": "Informática", "estado": "disponible", "ubicacion": "Almacén A"},
    {"codigo": "MON001", "nombre": "Monitor Dell 27'", "categoria": "Informática", "estado": "disponible", "ubicacion": "Almacén B"},
    {"codigo": "MON002", "nombre": "Monitor LG UltraWide", "categoria": "Informática", "estado": "disponible", "ubicacion": "Almacén B"},
    {"codigo": "CAM001", "nombre": "Cámara Canon EOS", "categoria": "Audiovisual", "estado": "disponible", "ubicacion": "Almacén C"},
    {"codigo": "CAM002", "nombre": "Cámara Sony A7", "categoria": "Audiovisual", "estado": "disponible", "ubicacion": "Almacén C"},
    {"codigo": "MIC001", "nombre": "Micrófono Blue Yeti", "categoria": "Audiovisual", "estado": "disponible", "ubicacion": "Almacén C"},
    {"codigo": "TAB001", "nombre": "iPad Pro 12.9", "categoria": "Tablets", "estado": "disponible", "ubicacion": "Almacén D"},
    {"codigo": "TAB002", "nombre": "Samsung Galaxy Tab", "categoria": "Tablets", "estado": "disponible", "ubicacion": "Almacén D"},
]
materiales = []
for data in materiales_data:
    m = Material.objects.create(**data)
    materiales.append(m)
    print(f"  ✅ {m.codigo}: {m.nombre}")
print(f"✅ {len(materiales)} materiales\n")

# USUARIOS
print("👥 Creando usuarios...")
usuarios_data = [
    {"dni": "12345678A", "nombre": "Ana", "apellidos": "García López", "email": "ana@egibide.org", "telefono": "600111222", "tipo_usuario": "estudiante"},
    {"dni": "23456789B", "nombre": "Carlos", "apellidos": "Martínez", "email": "carlos@egibide.org", "telefono": "600222333", "tipo_usuario": "estudiante"},
    {"dni": "34567890C", "nombre": "Elena", "apellidos": "Fernández", "email": "elena@egibide.org", "telefono": "600333444", "tipo_usuario": "estudiante"},
    {"dni": "45678901D", "nombre": "David", "apellidos": "López", "email": "david@egibide.org", "telefono": "600444555", "tipo_usuario": "estudiante"},
    {"dni": "56789012E", "nombre": "María", "apellidos": "Álvarez", "email": "maria@egibide.org", "telefono": "600555666", "tipo_usuario": "profesor"},
    {"dni": "67890123F", "nombre": "José", "apellidos": "Ramírez", "email": "jose@egibide.org", "telefono": "600666777", "tipo_usuario": "profesor"},
    {"dni": "78901234G", "nombre": "Carmen", "apellidos": "Torres", "email": "carmen@egibide.org", "telefono": "600777888", "tipo_usuario": "empleado"},
    {"dni": "89012345H", "nombre": "Miguel", "apellidos": "Rodríguez", "email": "miguel@egibide.org", "telefono": "600888999", "tipo_usuario": "empleado"},
]
usuarios = []
for data in usuarios_data:
    u = Usuario.objects.create(**data)
    usuarios.append(u)
    print(f"  ✅ {u.dni}: {u.nombre}")
print(f"✅ {len(usuarios)} usuarios\n")

# PRÉSTAMOS
print("📋 Creando préstamos...")
hoy = date.today()
prestamos_data = [
    {"codigo": "PRES001", "material": materiales[0], "usuario": usuarios[0], "fecha_prestamo": hoy - timedelta(days=5), "fecha_prevista_devolucion": hoy + timedelta(days=10), "estado": "prestado"},
    {"codigo": "PRES002", "material": materiales[1], "usuario": usuarios[1], "fecha_prestamo": hoy - timedelta(days=3), "fecha_prevista_devolucion": hoy + timedelta(days=7), "estado": "prestado"},
    {"codigo": "PRES003", "material": materiales[2], "usuario": usuarios[2], "fecha_prestamo": hoy - timedelta(days=20), "fecha_prevista_devolucion": hoy - timedelta(days=5), "estado": "retrasado"},
    {"codigo": "PRES004", "material": materiales[3], "usuario": usuarios[3], "fecha_prestamo": hoy - timedelta(days=30), "fecha_prevista_devolucion": hoy - timedelta(days=10), "fecha_real_devolucion": hoy - timedelta(days=8), "estado": "devuelto"},
    {"codigo": "PRES005", "material": materiales[5], "usuario": usuarios[4], "fecha_prestamo": hoy - timedelta(days=2), "fecha_prevista_devolucion": hoy + timedelta(days=5), "estado": "prestado"},
]
prestamos = []
for data in prestamos_data:
    mat = data['material']
    p = Prestamo.objects.create(**data)
    # Actualizar estado del material
    if data['estado'] in ['prestado', 'retrasado']:
        Material.objects.filter(pk=mat.pk).update(estado=data['estado'])
    prestamos.append(p)
    print(f"  ✅ {p.codigo}: {mat.nombre} → {p.usuario.nombre} [{p.estado}]")
print(f"✅ {len(prestamos)} préstamos\n")

# INCIDENCIAS
print("⚠️  Creando incidencias...")
incidencias_data = [
    {"codigo": "INC001", "fecha": hoy - timedelta(days=2), "descripcion": "Cable deteriorado", "tipo_incidencia": "daño", "prestamo": prestamos[0]},
    {"codigo": "INC002", "fecha": hoy - timedelta(days=5), "descripcion": "Funda extraviada", "tipo_incidencia": "pérdida", "prestamo": prestamos[2]},
    {"codigo": "INC003", "fecha": hoy - timedelta(days=1), "descripcion": "Pantalla rayada", "tipo_incidencia": "daño", "prestamo": prestamos[4]},
]
for data in incidencias_data:
    i = Incidencia.objects.create(**data)
    print(f"  ✅ {i.codigo}: {i.tipo_incidencia}")
print(f"✅ {len(incidencias_data)} incidencias\n")

print("=" * 50)
print("🎉 BASE DE DATOS POBLADA")
print(f"📦 Materiales: {Material.objects.count()}")
print(f"👥 Usuarios: {Usuario.objects.count()}")
print(f"📋 Préstamos: {Prestamo.objects.count()}")
print(f"⚠️  Incidencias: {Incidencia.objects.count()}")
print("=" * 50)

