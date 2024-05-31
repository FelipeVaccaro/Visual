import requests
from django.shortcuts import redirect, render
from django.conf import settings

def init_transaction(request):
    amount = 1000
    buy_order = "orden_compra_12345"
    session_id = request.session.session_key
    return_url = request.build_absolute_uri('/transaction/return/')

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