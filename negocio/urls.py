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
    path('pages/<int:pk>/', views.ProductDetail.as_view(), name='product_detail'), # Requisito: Route pages/
    path('pages/borrar/<int:pk>/', views.ProductDelete.as_view(), name='product_delete'),
    path('pages/editar/<int:pk>/', views.ProductUpdate.as_view(), name='product_update'),
    path('producto/<int:pk>/', views.ProductDetail.as_view(), name='product_detail'),
    path('producto/<int:pk>/borrar/', views.ProductDelete.as_view(), name='product_delete'),
    path('about/', views.about, name='about'),
    path('pages/', views.home, name='pages'),
    path('pages/editar/<int:pk>/', views.ProductUpdate.as_view(), name='product_update'),
    path('pages/borrar/<int:pk>/', views.ProductDelete.as_view(), name='product_delete'),
    path('lana/<int:pk>/', views.LanaDetail.as_view(), name='lana_detail'),
    path('lana/editar/<int:pk>/', views.LanaUpdate.as_view(), name='lana_update'),
    path('lana/borrar/<int:pk>/', views.LanaDelete.as_view(), name='lana_delete'),
    path('herramienta/<int:pk>/', views.HerramientaDetail.as_view(), name='herramienta_detail'),
    path('herramienta/editar/<int:pk>/', views.HerramientaUpdate.as_view(), name='herramienta_update'),
    path('herramienta/borrar/<int:pk>/', views.HerramientaDelete.as_view(), name='herramienta_delete'),  
]