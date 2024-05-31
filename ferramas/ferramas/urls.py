from django.contrib import admin
from django.urls import path, include
from . import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tienda.urls', namespace="tienda")),
    path('carrito/', include('carrito.urls', namespace="carrito")),
    path('transacciones/', include('transbank_api.urls', namespace="transbank")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
