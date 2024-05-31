from django.contrib import admin
from .models import usuario, CategoriaProd, Orden
# Register your models here.
admin.site.register(usuario)
admin.site.register(CategoriaProd)
admin.site.register(Orden)

class CategoriaProdAdmin(admin.ModelAdmin):
    
    readonly_fields=("created","updated")
    
class ProductoAdmin(admin.ModelAdmin):
    
    readonly_fields=("created","updated")




