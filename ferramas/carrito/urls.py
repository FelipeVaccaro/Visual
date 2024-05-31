from django.urls import path
from . import views

app_name="carrito"

urlpatterns = [
    path('', views.ver_carrito, name='ver_carrito'),
    path('agregar_al_carrito/<int:producto_id>/', views.agregar_producto, name='agregar_al_carrito'),
    path('eliminar_del_carrito/<int:producto_id>/', views.eliminar_producto, name='eliminar_del_carrito'),
    path('restar_del_carrito/<int:producto_id>/', views.restar_producto, name='restar_del_carrito'),
    path('limpiar_carrito/', views.limpiar, name='limpiar_carrito'),
]
