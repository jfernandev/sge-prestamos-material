from django.urls import path
from . import views

urlpatterns = [
    path('', views.MaterialListView.as_view(), name='material_list'),
    path('nuevo/', views.MaterialCreateView.as_view(), name='material_create'),
    path('<int:pk>/', views.MaterialDetailView.as_view(), name='material_detail'),
    path('<int:pk>/editar/', views.MaterialUpdateView.as_view(), name='material_update'),
    path('<int:pk>/borrar/', views.MaterialDeleteView.as_view(), name='material_delete'),
]

