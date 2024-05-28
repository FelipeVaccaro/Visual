"""
URL configuration for ferramas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from tienda.views import inicio, inicio_sesion, registro, home, nosotros, validacion_login, registrar_usuario, error_404, cierre_sesion, herramientas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('catalogo', herramientas),
    path('inicio', inicio),
    path('inicio-sesion', inicio_sesion, name='inicio-sesion'),
    path('registro', registro),
    path('nosotros', nosotros),
    path('404', error_404),
    path('validacion-login', validacion_login), #el loginpage usa validacion-login para autenticar al usuario del form
    path('registrar-usuario', registrar_usuario),
    path('cierre-sesion', cierre_sesion, name='cierre-sesion'),
    
]
