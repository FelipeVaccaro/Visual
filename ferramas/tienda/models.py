from django.db import models

class usuario(models.Model):
    usuario = models.CharField(primary_key=True, max_length=100, default='null', verbose_name='usuario')
    contrasena = models.CharField(max_length=32, default='null', verbose_name='contrasena')
    estado = models.BooleanField(null=False, blank=False, default=True, verbose_name='Estado usuarios') #Por si quiero desactivar usuarios

    class Meta:
        verbose_name='usuario'
        verbose_name_plural='usuarios'

    def __str__(self):
        return self.usuario