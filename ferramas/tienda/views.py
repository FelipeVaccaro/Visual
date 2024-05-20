from django.http import HttpResponse
from django.shortcuts import render, redirect
from requests import Response
from tienda.models import usuario
from django.contrib.auth import login, logout, authenticate
# Create your views here.

#FRONT
def catalogo(request):
    return render(request,'catalogo.html')

def inicio(request):
    return render(request,'inicio.html')

def login(request):
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
        return redirect('/login')
    else:
        mensaje = 'Las contraseñas no coinciden.'
        return HttpResponse(mensaje)

#-----------------Fin registro data BBDD-----------------

#--------------Validación Login -------------------------

def validacion_login(request):
    # try:
        usuario_entrante = request.POST.get('usuario')
        passw_entrante = request.POST.get('contrasena')

        # Verifica si el usuario existe en la base de datos
        usr_encontrado = usuario.objects.get(usuario=usuario_entrante)
        passw_entrante = usuario.objects.get(contrasena=passw_entrante)
        # usr_encontrado = authenticate(username=usuario.objects.get(usuario=usuario_entrante), password=usuario.objects.get(usuario=passw_entrante))
        print("usr encontrado: ",usr_encontrado)
        print("passw encontrado: ",passw_entrante)
        user = authenticate(username=usuario_entrante, password=passw_entrante)
        print("user: ",user)
        # Verifica si la contraseña coincide
        # if usr_encontrado.contrasena == passw_entrante:
        # if usr_encontrado:
        if user is None:
            login(request)
            print("login: ",request.user)
            return redirect('/inicio')
        else:
            print("else")
            # Si la contraseña no coincide, devuelve un error
            return HttpResponse(status=404)
    # except usuario.DoesNotExist:
    #     # Si el usuario no existe, devuelve un error
    #     print("except")
    #     return HttpResponse(status=404)

#-----------------Fin Validación Login ---------------------

def cierre_sesion(request):
    logout(request)
    print("logout: ",request.user)
    return redirect('/')
