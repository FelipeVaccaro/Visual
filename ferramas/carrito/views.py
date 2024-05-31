from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .carrito import Carrito
from tienda.functions import data_from_api
import requests

# Create your views here.

def total_carrito(request):
    return render(request, "carrito.html", {})

def agregar_producto(request, producto_id):
    producto = data_from_api()

    for prod in producto:
        if prod['ID_HERRAMIENTA'] == producto_id:
            producto = prod
            break

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

# Transbank API CONNECTION
def init_transaction(request,total):
    amount = total  # Monto de la transacción
    buy_order = "orden_compra_12345"  # Número de orden único
    session_id = request.session.session_key
    return_url = request.build_absolute_uri('/carrito/return/')

    response = requests.post('http://localhost:5000/api/init_transaction', json={
        'amount': amount,
        'buy_order': buy_order,
        'session_id': session_id,
        'return_url': return_url
    })
    data = response.json()
    return redirect(data['url'] + '?token_ws=' + data['token'])

def transaction_return(request):
    token = request.GET.get('token_ws')

    response = requests.post('http://localhost:5000/api/transaction_return', json={
        'token_ws': token
    })

    data = response.json()

    if data['status'] == 'AUTHORIZED':
        # Manejar el éxito de la transacción
        context = {
            'response': data
        }
        return render(request, 'transaccion_exitosa.html', context)
    else:
        # Manejar el error de la transacción
        context = {
            'response': data
        }
        return render(request, 'transaccion_fallida.html', context)