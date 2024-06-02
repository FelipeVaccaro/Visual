from django.urls import path
from . import views
from . import functions

app_name="tienda"

urlpatterns = [
    path('', views.inicio, name='home'),
    path('catalogo/', views.catalogo_productos, name='catalogo'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('404/', views.error_404),
    path('inicio-sesion/', views.login_usuario, name='login'),
    path('cierre-sesion/', views.cierre_sesion, name='logout'),
    path('registro/', views.registro, name='registro'),
    path('comprar/', views.comprar, name='comprar'),
]