from django.urls import path
from . import views

# Si tenías una línea que decía "app_name = ...", BORRALA.
# Django se confunde si pones eso y no lo usas en el HTML.

urlpatterns = [
    # Esta es la linea que está fallando ahora:
    path('', views.home, name='inicio'), 
    
    # Estas son las que fallaban antes:
    path('crear_lana/', views.crear_lana, name='crear_lana'),
    path('crear_herramienta/', views.crear_herramienta, name='crear_herramienta'),
    path('crear_cliente/', views.crear_cliente, name='crear_cliente'),
    path('buscar_lana/', views.buscar_lana, name='buscar_lana'),
    path('crear-producto/', views.crear_producto, name='crear_producto'),
]