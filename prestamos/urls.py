from django.urls import path
from . import views

urlpatterns = [
    path('', views.PrestamoListView.as_view(), name='prestamo_list'),
    path('nuevo/', views.PrestamoCreateView.as_view(), name='prestamo_create'),
    path('<int:pk>/', views.PrestamoDetailView.as_view(), name='prestamo_detail'),
    path('<int:pk>/editar/', views.PrestamoUpdateView.as_view(), name='prestamo_update'),
    path('<int:pk>/cerrar/', views.PrestamoCerrarView.as_view(), name='prestamo_cerrar'),
    path('<int:pk>/borrar/', views.PrestamoDeleteView.as_view(), name='prestamo_delete'),
]

