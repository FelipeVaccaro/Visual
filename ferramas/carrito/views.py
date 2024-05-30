from django.shortcuts import render
from .carrito import Carro
from tienda.models import Producto
from django.shortcuts import redirect

# Create your views here.

def agregar_producto(request, producto_id):
    carro=Carro(request)
    Producto=Producto.objetcts.get(producto_id)
    carro.agregar(producto=Producto)
    return redirect("Tienda")

def eliminar_producto(request, producto_id):
    carro=Carro(request)
    Producto=Producto.objetcts.get(producto_id)
    carro.eliminar(producto=Producto)
    return redirect("Tienda")

def restar_producto(request, producto_id):
    carro=Carro(request)
    Producto=Producto.objetcts.get(producto_id)
    carro.restar_producto(producto=Producto)
    return redirect("Tienda")

def limpiar_carro(request):
    carro=Carro(request)
    carro.limpiar_carro()
    return redirect("Tienda")