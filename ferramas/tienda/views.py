from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from requests import Response
from tienda.models import usuario
from django.contrib.auth import login, logout, authenticate
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


#--------------Registro de data BBDD-------------------

def registrar_usuario(request):
    print("request: ", request)
    #obtiene datos desde el formulario en registro
    registro_correo = request.POST.get('registro_email')
    registro_pass1 = request.POST.get('registro_pass1')
    registro_pass2 = request.POST.get('registro_pass2')
    if registro_pass1 == registro_pass2:
    #Registra al usuario en la BBDD
        nuevo_usuario=usuario()
        nuevo_usuario.usuario=registro_correo
        nuevo_usuario.contrasena=registro_pass1
        usuario.save(nuevo_usuario)
        return redirect('/inicio-sesion')
    else:
        mensaje = 'Las contraseñas no coinciden.'
        return HttpResponse(mensaje)

#-----------------Fin registro data BBDD-----------------

#--------------Validación Login -------------------------

def validacion_login(request):
    usuario_entrante = request.POST.get('usuario')
    passw_entrante = request.POST.get('contrasena')

    # Verifica si el usuario existe en la base de datos
    try:
        usr_encontrado = usuario.objects.get(usuario=usuario_entrante)
    except usuario.DoesNotExist:
        return HttpResponse(status=404)

    # Autentica al usuario
    user = authenticate(request, username=usuario_entrante, password=passw_entrante)
    if user is not None:
        user.is_authenticated = True
        login(request, user)
        return render(request, 'inicio.html')
    else:
        return HttpResponse(status=404)

#-----------------Fin Validación Login ---------------------

def cierre_sesion(request):
    logout(request)
    print("logout: ",request.user)
    if request.user.is_authenticated:
        request.user.is_authenticated = False
    else:
        return redirect('/')
