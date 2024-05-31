from django.urls import path
from . import views


app_name="carrito"

urlpatterns = [
    path('', views.total_carrito, name="total_carrito"),
    path("agregar/<int:producto_id>/", views.agregar_producto, name ="carrito_agregar"),
    path("eliminar/<int:producto_id>/", views.eliminar_producto, name ="carrito_eliminar"),
    path("restar/<int:producto_id>/", views.restar_producto, name ="carrito_restar"),
    path("limpiar/", views.limpiar_carro, name ="carrito_limpiar"),
]
