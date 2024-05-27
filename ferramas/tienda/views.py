from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

#FRONT

def materiales(request):
    return render(request, 'materiales-catalogo.html')

def herramientas(request):
    return render(request, 'herramientas-catalogo.html')

def equiposg(request):
    return render(request, 'equiposg-catalogo.html')

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
            form.save()
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            if password == password2:
                user = authenticate(request, username=email, password=password)
                return redirect('/inicio-sesion', messages)
            else:
                error_msj = messages.error(request, 'Las contraseñas no coinciden.')
                return render(request, 'registro.html', {'title': error_msj})
        else:
            error_msj = messages.error(request, str(form.errors))
            return render(request, 'registro.html', {'title': error_msj})
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
            return redirect('/', messages)
        
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