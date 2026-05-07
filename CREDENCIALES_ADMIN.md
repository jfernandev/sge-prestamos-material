# 🔐 Credenciales de Administración

## Superusuario del Admin Django

Para acceder al panel de administración en http://localhost:8000/admin/

**Usuario:** admin  
**Contraseña:** [ANOTAR AQUÍ TU CONTRASEÑA]

---

## 📝 Instrucciones para el equipo

### Si ya tienes el proyecto clonado:

```bash
# 1. Descargar los últimos cambios (incluyendo la BD)
git pull origin main

# 2. Activar entorno virtual
source venv/bin/activate

# 3. Lanzar el servidor
python manage.py runserver
```

### Si acabas de clonar el proyecto:

```bash
# 1. Clonar repositorio
git clone https://github.com/jfernandev/sge-prestamos-material.git
cd sge-prestamos-material

# 2. Crear y activar entorno virtual
python3 -m venv venv
source venv/bin/activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Lanzar servidor (NO necesitas hacer migraciones ni crear superusuario)
python manage.py runserver
```

---

## ⚠️ IMPORTANTE

- La base de datos `db.sqlite3` se comparte entre todos los desarrolladores
- Cualquier cambio que hagas (crear/editar/borrar materiales, usuarios, etc.) afectará a todos
- Si borras datos por error, afectará al equipo completo
- **Coordinarse antes de hacer cambios importantes**

---

## 🔄 Sincronizar cambios

Antes de empezar a trabajar cada día:
```bash
git pull origin main
```

Después de hacer cambios:
```bash
git add .
git commit -m "descripción de cambios"
git push origin main
```

---

📅 Proyecto SGE - Reto 9 | 🎓 Egibide 2026

