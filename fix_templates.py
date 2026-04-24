#!/usr/bin/env python3
import os
import sys

BASE = "/Users/jonherrera/SistemasGestionEmpresarial/Python/sge-prestamos-material"

files = {
    f"{BASE}/materiales/templates/materiales/material_detail.html": """{% extends 'base.html' %}
{% block content %}
<h1>Detalle de material</h1>
<ul>
    <li><strong>Código:</strong> {{ object.codigo }}</li>
    <li><strong>Nombre:</strong> {{ object.nombre }}</li>
    <li><strong>Descripción:</strong> {{ object.descripcion }}</li>
    <li><strong>Categoría:</strong> {{ object.categoria }}</li>
    <li><strong>Estado:</strong> {{ object.estado }}</li>
    <li><strong>Ubicación:</strong> {{ object.ubicacion }}</li>
    <li><strong>Fecha de alta:</strong> {{ object.fecha_alta }}</li>
</ul>
<a href="{% url 'material_update' object.pk %}" class="btn">Editar</a>
<a href="{% url 'material_delete' object.pk %}" class="btn" style="background-color: #f44336;">Borrar</a>
<a href="{% url 'material_list' %}" class="btn" style="background-color: #008CBA;">Volver</a>
{% endblock %}""",

    f"{BASE}/prestamos/templates/prestamos/prestamo_detail.html": """{% extends 'base.html' %}
{% block content %}
<h1>Detalle de préstamo</h1>
<ul>
    <li><strong>Código:</strong> {{ object.codigo }}</li>
    <li><strong>Material:</strong> {{ object.material.nombre }}</li>
    <li><strong>Usuario:</strong> {{ object.usuario.nombre }} {{ object.usuario.apellidos }}</li>
    <li><strong>Fecha préstamo:</strong> {{ object.fecha_prestamo }}</li>
    <li><strong>Fecha prevista devolución:</strong> {{ object.fecha_prevista_devolucion }}</li>
    <li><strong>Fecha real devolución:</strong> {{ object.fecha_real_devolucion|default:"Pendiente" }}</li>
    <li><strong>Estado:</strong> {{ object.estado }}</li>
    <li><strong>Observaciones:</strong> {{ object.observaciones }}</li>
</ul>
<a href="{% url 'prestamo_update' object.pk %}" class="btn">Editar</a>
{% if object.estado != 'devuelto' %}
<a href="{% url 'prestamo_cerrar' object.pk %}" class="btn">Cerrar</a>
{% endif %}
<a href="{% url 'prestamo_delete' object.pk %}" class="btn" style="background-color:#f44336;">Borrar</a>
<a href="{% url 'prestamo_list' %}" class="btn" style="background-color:#008CBA;">Volver</a>
{% endblock %}""",

    f"{BASE}/prestamos/templates/prestamos/prestamo_form.html": """{% extends 'base.html' %}
{% block content %}
<h1>{% if object %}Editar{% else %}Nuevo{% endif %} préstamo</h1>
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Guardar</button>
    <a href="{% url 'prestamo_list' %}" class="btn" style="background-color:#808080;">Cancelar</a>
</form>
{% endblock %}"""
}

try:
    for path, content in files.items():
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        size = os.path.getsize(path)
        print(f"✓ {os.path.basename(path)} ({size} bytes)")
    print("\n✅ Todos los archivos completados correctamente!")
    sys.exit(0)
except Exception as e:
    print(f"❌ Error: {e}")
    sys.exit(1)

