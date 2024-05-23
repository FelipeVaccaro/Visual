from django.contrib.auth.backends import BaseBackend
from .models import usuario

class MiBackendDeAutenticacion(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        usr_encontrado = usuario.objects.get(usuario=username)
        passw_encontrada = usr_encontrado.contrasena
        if usr_encontrado and password == passw_encontrada:
            usr_encontrado.is_authenticated = True
            usr_encontrado.save()
            return usr_encontrado
        else:
            return None

    def is_authenticated(self, request):
        return request.user.is_authenticated

    def logout(self, request):
        try:
            request.user.is_authenticated = False
            request.user.save()
            return True
        except:
            return False