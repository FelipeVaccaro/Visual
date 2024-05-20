from django.contrib.auth.backends import BaseBackend
from .models import usuario

class MiBackendDeAutenticacion(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        usr_encontrado = usuario.objects.get(usuario=username)
        passw_entrante = usr_encontrado.contrasena

        if usr_encontrado and password == passw_entrante:
            return usr_encontrado
        else:
            return None