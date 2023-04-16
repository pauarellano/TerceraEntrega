from django.urls import path
from .views import *

urlpatterns = [
    path('Registro/', crear_cliente, name="Registro"),
    path('',inicio,name="inicio app"),
    path("Clientes/",clientes, name="Clientes"),
    path("Carrito/",carrito, name="Carrito"),
    path("Articulos/",articulos, name="Articulos"),
    path("buscarArticulo/",buscarArticulo, name="buscarArticulo"),
    path("buscandoArticulo/",buscandoArticulo, name="buscandoArticulo"),
]