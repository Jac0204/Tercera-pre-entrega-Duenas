from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cliente', views.cliente, name='cliente'),
    path('cliente/buscar_cliente', views.buscar_cliente, name='buscar_cliente'),
    path('categoria', views.categoria, name='categoria'),
    path('categoria/buscar_categoria', views.buscar_categoria, name='buscar_categoria'),
    path('producto', views.producto, name='producto'),
    path('producto/buscar_producto', views.buscar_producto, name='buscar_producto'),
]