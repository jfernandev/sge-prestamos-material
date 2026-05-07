"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter

from materiales.views import MaterialViewSet
from usuarios.views import UsuarioViewSet
from prestamos.views import PrestamoViewSet
from incidencias.views import IncidenciaViewSet

# Router para la API REST
router = DefaultRouter()
router.register(r'materiales', MaterialViewSet, basename='material')
router.register(r'usuarios', UsuarioViewSet, basename='usuario')
router.register(r'prestamos', PrestamoViewSet, basename='prestamo')
router.register(r'incidencias', IncidenciaViewSet, basename='incidencia')

urlpatterns = [
    # Frontend (home page) - Aquí se cargará Vue.js
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('inicio/', TemplateView.as_view(template_name='home.html'), name='inicio'),
    
    # Admin Django
    path('admin/', admin.site.urls),
    
    # API REST
    path('api/', include(router.urls)),
]
