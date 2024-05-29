from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

#FRONT

def herramientas(request):
    return render(request, 'catalogo.html')

def inicio(request):
    return render(request,'inicio.html')

def inicio_sesion(request):
    return render(request,'login.html')

def registro(request):
    return render(request,'registro.html')

def home(request):
    return render(request, 'inicio.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def error_404(request, exception=None):
    return render(request, '404.html', status=404)


#--------------Registro de data BBDD 2-------------------

def registrar_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Hubo un problema en el registro. Por favor, verifica los datos ingresados')
    else:
        form = UserCreationForm()
    return render(request, 'registro.html', {'form': form})

#-----------------Fin registro data BBDD 2-----------------


#--------------Validación Login -------------------------

def validacion_login(request):
    if request.method == 'POST':
        email = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Inicio de sesión exitoso')
            return redirect('/')
        
        else:
            error_msj= messages.error(request, 'Usuario o contraseña incorrecta')
            return render(request, 'login.html', {'title': error_msj })
    else:
        return render(request, 'login.html')

#----------------- FIN Validación Login ---------------------

#----------------- Cerrar Sesión -----------------------------

def cierre_sesion(request):
    logout(request)
    print("logout: ",request.user)
    if request.user.is_authenticated:
        request.user.is_authenticated = False
    else:
        return redirect('/')

#----------------- Fin Cerrar Sesión -----------------------------