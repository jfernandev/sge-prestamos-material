from django.urls import path
from . import views

urlpatterns = [
    path('', views.IncidenciaListView.as_view(), name='incidencia_list'),
    path('nuevo/', views.IncidenciaCreateView.as_view(), name='incidencia_create'),
    path('<int:pk>/', views.IncidenciaDetailView.as_view(), name='incidencia_detail'),
    path('<int:pk>/editar/', views.IncidenciaUpdateView.as_view(), name='incidencia_update'),
    path('<int:pk>/borrar/', views.IncidenciaDeleteView.as_view(), name='incidencia_delete'),
]

