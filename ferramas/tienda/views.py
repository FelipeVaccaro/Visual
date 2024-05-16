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