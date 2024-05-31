from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .carrito import Carrito
from tienda.functions import data_from_api

# Create your views here.

def total_carrito(request):
    return render(request, "carrito.html", {})

def agregar_producto(request, producto_id):
    producto = data_from_api()

    for prod in producto:
        if prod['ID_HERRAMIENTA'] == producto_id:
            producto = prod
            break
        print(prod)

    if not producto:
        return JsonResponse({'error': 'Producto no encontrado'}, status=404)
    
    carrito=Carrito(request)
    carrito.agregar(producto)

    return redirect('carrito:ver_carrito')

def ver_carrito(request):
    carrito = Carrito(request)
    total = carrito.obtener_total()
    items = carrito.obtener_items()
    return render(request, 'carrito.html', {'carrito': items, 'total': total})

def eliminar_producto(request, producto_id):
    carrito=Carrito(request)
    carrito.eliminar(producto_id)
    return redirect("carrito:ver_carrito")

def restar_producto(request, producto_id):
    carrito=Carrito(request)
    carrito.restar_producto(producto_id)
    return redirect("carrito:ver_carrito")

def limpiar(request):
    carrito=Carrito(request)
    carrito.limpiar()
    return redirect("carrito:ver_carrito")