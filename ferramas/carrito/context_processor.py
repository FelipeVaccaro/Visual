from .carrito import Carrito

# Crear un context processor para que el carrito funcione en todas las páginas
def carrito(request):
    return {'cart': Carrito(request)}


def importe_total_carro(request):
    total=0
    if request.user.is_authenticated:
        for key, value in request.session["carro"].items():
            total = total+float(value["precio"])
        return {"importe_total_carro":total}
            