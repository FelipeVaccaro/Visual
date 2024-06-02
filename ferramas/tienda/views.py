from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render
from carrito.carrito import Carrito
from .functions import data_from_api
from .forms import FormularioRegistro
# Create your views here.

#FRONT

def catalogo_productos(request):
    datos_herramientas = data_from_api()
    return render(request, 'catalogo.html', {'datos_herramientas': datos_herramientas})

def inicio(request):
    return render(request,'inicio.html')

def home(request):
    return render(request, 'inicio.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def error_404(request, exception=None):
    return render(request, '404.html', status=404)

def registro(request):
    form = FormularioRegistro()
    if request.method == "POST":
        form = FormularioRegistro(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            #log in usuario
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Te has registrado"))
            return redirect('tienda:home')
        else:
            print(request)
            messages.success(request, (" Hubo un problema"))
            return redirect('tienda:registro')
    else:
            return render(request, 'registro.html', {'form':form})

def login_usuario(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Inicio de sesión exitoso')
            return redirect('tienda:home')
        else:
            messages.error(request, 'Usuario o contraseña incorrecta')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html', {})

#----------------- FIN Validación Login ---------------------

#----------------- Cerrar Sesión -----------------------------

def cierre_sesion(request):
    logout(request)
    if request.user.is_authenticated:
        request.user.is_authenticated = False
    else:
        return redirect('tienda:home')

#----------------- Fin Cerrar Sesión -----------------------------

def comprar(request):
    carrito = Carrito(request)
    items = carrito.obtener_items()
    total = carrito.obtener_total()
    carrito.limpiar()

    return render(request, 'comprar.html', {'total': total, 'items': items})