import datetime
from django.db import models

class usuario(models.Model):
    usuario = models.CharField(max_length=100, verbose_name='usuario')
    contrasena = models.CharField(max_length=32, default='null', verbose_name='contrasena')
    estado = models.BooleanField(null=False, blank=False, default=True, verbose_name='Estado usuarios') #Por si quiero desactivar usuarios
    last_login = models.DateTimeField(auto_now=True)
    is_authenticated = models.BooleanField(default=False)

    class Meta:
        verbose_name='usuario'
        verbose_name_plural='usuarios'

    def __str__(self):
        return self.usuario
    
#Categoria productos--------------------------------

class CategoriaProd(models.Model):
    nombre=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name="categoriaProd"
        verbose_name_plural="categoriasProd"
        
    def __str__(self) -> str:
        return self.nombre
    
#Modelo de la orden-----------------------------
class Orden(models.Model):
    producto= models.IntegerField(default=1)
    cantidad= models.IntegerField(default=1)
    direccion= models.CharField(max_length=100, default='', blank=True)
    telefono= models.CharField(max_length=20, default='', blank=True)
    fecha=models.DateField(default=datetime.datetime.today)
    estado= models.BooleanField(default=False)

    def __str__(self):
        return self.producto

