from django.shortcuts import render
from .carrito import Carro
from django.shortcuts import redirect

# Create your views here.

def total_carrito(request):
    return render(request, "total_carrito.html", {})

def agregar_producto(request, producto_id):
    carro=Carro(request)
    producto=Producto.objects.get(producto_id)
    carro.agregar(producto)
    return redirect("tienda")

def eliminar_producto(request, producto_id):
    carro=Carro(request)
    producto=Producto.objects.get(producto_id)
    carro.eliminar(producto)
    return redirect("tienda")

def restar_producto(request, producto_id):
    carro=Carro(request)
    Producto=Producto.objects.get(producto_id)
    carro.restar_producto(producto=Producto)
    return redirect("tienda")

def limpiar_carro(request):
    carro=Carro(request)
    carro.limpiar_carro()
    return redirect("tienda")