from django.shortcuts import render

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

def validacion_login(request, usuario):
    print('Resultado de request: ',request) #aqui adaptar segun tu base de datos
    try:
        usuarios = usuarios.objects.get(usuario=usuario)
    except usuarios.DoesNotExist:
        return Response({'messaje':'El supervisor buscado no existe en nuestros registros'},status=status.HTTP_404_NOT_FOUND)
    
    usr_entrante = request.data['usuario']
    passw_entrante = request.data['contrasena']
    usr_encontrado = usuarios.objects.get(usuario = usr_entrante) #lo va a buscar que el usuario sea igual al usuario entrante
    passw_encontrada = usr_encontrado.contrasena
    if(passw_encontrada == passw_entrante):
        return Response({'message':'ok'},status=status.HTTP_200_OK)
    else: 
        return Response({'message':'Información errónea, intente nuevamente'},status=status.HTTP_400_BAD_REQUEST)
