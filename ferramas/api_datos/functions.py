from django.shortcuts import render
import requests

def data_from_api(request):
    url = ('http://127.0.0.1:5000/tools/')
    response = requests.get(url)

    try:
        response.status_code == 200
        data = response.json()
    except:
        data = []
    print(data)

    context = {'datos_herramientas': data}
    return render(request, 'catalogo.html', context)