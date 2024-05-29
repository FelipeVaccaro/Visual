from django.contrib import admin
from django.urls import path
from . import views
from tienda.views import inicio, inicio_sesion, registro, home, nosotros, validacion_login, registrar_usuario, error_404, cierre_sesion, catalogo_productos

app_name="tienda"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('catalogo/', catalogo_productos),
    path('inicio/', inicio),
    path('inicio-sesion/', inicio_sesion, name='inicio-sesion'),
    path('registro/', registro),
    path('nosotros/', nosotros),
    path('404/', error_404),
    path('validacion-login', validacion_login), #el loginpage usa validacion-login para autenticar al usuario del form
    path('registrar-usuario', registrar_usuario),
    path('cierre-sesion', cierre_sesion, name='cierre-sesion'), 
]