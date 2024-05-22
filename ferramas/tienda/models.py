from django.db import models

class usuario(models.Model):
    usuario = models.CharField(max_length=100, verbose_name='usuario')
    contrasena = models.CharField(max_length=32, default='null', verbose_name='contrasena')
    estado = models.BooleanField(null=False, blank=False, default=True, verbose_name='Estado usuarios') #Por si quiero desactivar usuarios
    last_login = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name='usuario'
        verbose_name_plural='usuarios'

    def __str__(self):
        return self.usuario