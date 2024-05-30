from django.contrib import admin
from django.urls import path
from . import views

app_name="tienda"

urlpatterns = [
    path('', views.inicio),
    path('inicio/', views.inicio),
    path('catalogo/', views.catalogo_productos),
    path('inicio-sesion/', views.inicio_sesion, name='inicio-sesion'),
    path('registro/', views.registro),
    path('nosotros/', views.nosotros),
    path('404/', views.error_404),
    path('validacion-login/', views.validacion_login), #el loginpage usa validacion-login para autenticar al usuario del form
    path('registrar-usuario/', views.registrar_usuario),
    path('cierre-sesion/', views.cierre_sesion, name='cierre-sesion'),
]