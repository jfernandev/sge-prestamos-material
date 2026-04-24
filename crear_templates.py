#!/usr/bin/env python3
# Script para crear todos los templates restantes

import os

# Rutas base
BASE_DIR = "/Users/jonherrera/SistemasGestionEmpresarial/Python/sge-prestamos-material"

# Templates de Prestamos
prestamo_templates = {
    "prestamo_detail.html": """{% extends 'base.html' %}
{% block content %}
<h1>Detalle de préstamo</h1>
<ul>
    <li><strong>Código:</strong> {{ object.codigo }}</li>
    <li><strong>Material:</strong> {{ object.material.nombre }}</li>
    <li><strong>Usuario:</strong> {{ object.usuario.nombre }} {{ object.usuario.apellidos }}</li>
    <li><strong>Fecha de préstamo:</strong> {{ object.fecha_prestamo }}</li>
    <li><strong>Fecha prevista de devolución:</strong> {{ object.fecha_prevista_devolucion }}</li>
    <li><strong>Fecha real de devolución:</strong> {{ object.fecha_real_devolucion|default:"Pendiente" }}</li>
    <li><strong>Estado:</strong> {{ object.estado }}</li>
    <li><strong>Observaciones:</strong> {{ object.observaciones }}</li>
</ul>
<a href="{% url 'prestamo_update' object.pk %}" class="btn">Editar</a>
{% if object.estado != 'devuelto' %}
<a href="{% url 'prestamo_cerrar' object.pk %}" class="btn">Cerrar préstamo</a>
{% endif %}
<a href="{% url 'prestamo_delete' object.pk %}" class="btn" style="background-color: #f44336;">Borrar</a>
<a href="{% url 'prestamo_list' %}" class="btn" style="background-color: #008CBA;">Volver al listado</a>
{% endblock %}
""",
    "prestamo_form.html": """{% extends 'base.html' %}
{% block content %}
<h1>{% if object %}Editar{% else %}Nuevo{% endif %} préstamo</h1>
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Guardar</button>
    <a href="{% url 'prestamo_list' %}" class="btn" style="background-color: #808080;">Cancelar</a>
</form>
{% endblock %}
""",
    "prestamo_cerrar.html": """{% extends 'base.html' %}
{% block content %}
<h1>Cerrar préstamo</h1>
<p>¿Confirmas que el material "{{ prestamo.material.nombre }}" ha sido devuelto por "{{ prestamo.usuario.nombre }} {{ prestamo.usuario.apellidos }}"?</p>
<form method="post">
    {% csrf_token %}
    <button type="submit">Sí, cerrar préstamo</button>
    <a href="{% url 'prestamo_list' %}" class="btn" style="background-color: #808080;">Cancelar</a>
</form>
{% endblock %}
""",
    "prestamo_confirm_delete.html": """{% extends 'base.html' %}
{% block content %}
<h1>Confirmar borrado</h1>
<p>¿Seguro que quieres borrar el préstamo "{{ object.codigo }}"?</p>
<form method="post">
    {% csrf_token %}
    <button type="submit" style="background-color: #f44336;">Sí, borrar</button>
    <a href="{% url 'prestamo_list' %}" class="btn" style="background-color: #808080;">Cancelar</a>
</form>
{% endblock %}
"""
}

# Templates de Incidencias
incidencia_templates = {
    "incidencia_list.html": """{% extends 'base.html' %}
{% block content %}
<h1>Incidencias</h1>
<a href="{% url 'incidencia_create' %}" class="btn">Nueva incidencia</a>
<table>
    <tr>
        <th>Código</th>
        <th>Fecha</th>
        <th>Tipo</th>
        <th>Préstamo</th>
        <th>Acciones</th>
    </tr>
    {% for incidencia in object_list %}
    <tr>
        <td>{{ incidencia.codigo }}</td>
        <td>{{ incidencia.fecha }}</td>
        <td>{{ incidencia.tipo_incidencia }}</td>
        <td>{{ incidencia.prestamo.codigo }}</td>
        <td>
            <a href="{% url 'incidencia_detail' incidencia.pk %}">Detalle</a> |
            <a href="{% url 'incidencia_update' incidencia.pk %}">Editar</a> |
            <a href="{% url 'incidencia_delete' incidencia.pk %}">Borrar</a>
        </td>
    </tr>
    {% endfor %}
</table>
{% endblock %}
""",
    "incidencia_detail.html": """{% extends 'base.html' %}
{% block content %}
<h1>Detalle de incidencia</h1>
<ul>
    <li><strong>Código:</strong> {{ object.codigo }}</li>
    <li><strong>Fecha:</strong> {{ object.fecha }}</li>
    <li><strong>Descripción:</strong> {{ object.descripcion }}</li>
    <li><strong>Tipo de incidencia:</strong> {{ object.tipo_incidencia }}</li>
    <li><strong>Préstamo asociado:</strong> <a href="{% url 'prestamo_detail' object.prestamo.pk %}">{{ object.prestamo.codigo }}</a></li>
</ul>
<a href="{% url 'incidencia_update' object.pk %}" class="btn">Editar</a>
<a href="{% url 'incidencia_delete' object.pk %}" class="btn" style="background-color: #f44336;">Borrar</a>
<a href="{% url 'incidencia_list' %}" class="btn" style="background-color: #008CBA;">Volver al listado</a>
{% endblock %}
""",
    "incidencia_form.html": """{% extends 'base.html' %}
{% block content %}
<h1>{% if object %}Editar{% else %}Nueva{% endif %} incidencia</h1>
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Guardar</button>
    <a href="{% url 'incidencia_list' %}" class="btn" style="background-color: #808080;">Cancelar</a>
</form>
{% endblock %}
""",
    "incidencia_confirm_delete.html": """{% extends 'base.html' %}
{% block content %}
<h1>Confirmar borrado</h1>
<p>¿Seguro que quieres borrar la incidencia "{{ object.codigo }}"?</p>
<form method="post">
    {% csrf_token %}
    <button type="submit" style="background-color: #f44336;">Sí, borrar</button>
    <a href="{% url 'incidencia_list' %}" class="btn" style="background-color: #808080;">Cancelar</a>
</form>
{% endblock %}
"""
}

# Crear templates de prestamos
prestamos_dir = os.path.join(BASE_DIR, "prestamos/templates/prestamos")
for filename, content in prestamo_templates.items():
    filepath = os.path.join(prestamos_dir, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Creado: {filename}")

# Crear templates de incidencias
incidencias_dir = os.path.join(BASE_DIR, "incidencias/templates/incidencias")
for filename, content in incidencia_templates.items():
    filepath = os.path.join(incidencias_dir, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Creado: {filename}")

print("\n✓ Todos los templates han sido creados correctamente")

