from django.contrib import admin
from .models import usuario, CategoriaProd, Producto
# Register your models here.
admin.site.register(usuario)

class CategoriaProdAdmin(admin.ModelAdmin):
    
    readonly_fields=("created","updated")
    
class ProductoAdmin(admin.ModelAdmin):
    
    readonly_fields=("created","updated")

admin.site.register(Producto)
admin.site.register(CategoriaProd)



