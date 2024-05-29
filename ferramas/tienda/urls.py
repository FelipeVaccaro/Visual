from django.urls import path
from . import views

app_name="tienda"

urlpatterns = [
    path('', views.home, name="index"),
    path('catalogo/', views.catalogo_productos),
    path('inicio/', views.inicio),
    path('inicio-sesion/', views.inicio_sesion, name='inicio-sesion'),
    path('cierre-sesion/', views.cierre_sesion, name='cierre-sesion'), 
    path('registro/', views.registro),
    path('nosotros/', views.nosotros),
    path('404/', views.error_404),
    path('validacion-login/', views.validacion_login), #el loginpage usa validacion-login para autenticar al usuario del form
    path('registrar-usuario/', views.registrar_usuario),
    # path("agregar/<int:producto_id>/", views.agregar_producto, name ="agregar"),
    # path("eliminar/<int:producto_id>/", views.eliminar_producto, name ="eliminar"),
    # path("restar/<int:producto_id>/", views.restar_producto, name ="restar"),
    # path("limpiar/", views.limpiar_carro, name ="limpiar"),
]
