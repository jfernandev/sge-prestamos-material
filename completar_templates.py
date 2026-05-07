#!/usr/bin/env python3
import os

BASE_DIR = "/Users/jonherrera/SistemasGestionEmpresarial/Python/sge-prestamos-material"

# Template prestamo_detail
prestamo_detail_content = """{% extends 'base.html' %}
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
"""

# Template prestamo_form
prestamo_form_content = """{% extends 'base.html' %}
{% block content %}
<h1>{% if object %}Editar{% else %}Nuevo{% endif %} préstamo</h1>
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Guardar</button>
    <a href="{% url 'prestamo_list' %}" class="btn" style="background-color: #808080;">Cancelar</a>
</form>
{% endblock %}
"""

# Escribir prestamo_detail
with open(os.path.join(BASE_DIR, "prestamos/templates/prestamos/prestamo_detail.html"), 'w', encoding='utf-8') as f:
    f.write(prestamo_detail_content)
print("✓ prestamo_detail.html actualizado")

# Escribir prestamo_form
with open(os.path.join(BASE_DIR, "prestamos/templates/prestamos/prestamo_form.html"), 'w', encoding='utf-8') as f:
    f.write(prestamo_form_content)
print("✓ prestamo_form.html actualizado")

print("\n✓ Todos los templates vacíos han sido completados")

