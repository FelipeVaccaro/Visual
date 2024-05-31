from decimal import Decimal


class Carrito:
    def __init__(self, request):
        self.session = request.session
        carrito=self.session.get("session_key")

        # Si el usuario es nuevo, no hay llave de sesión, entonces se crea una
        if 'session_key' not in request.session:
            carrito = self.session['session_key'] = {}
        self.carrito = carrito
    
    def agregar(self, producto):
        producto_id = (producto['ID_HERRAMIENTA'])

        if producto_id in self.carrito:
            self.carrito[producto_id]['cantidad'] +=1
        else:
            self.carrito[producto_id] = {
                'nombre': producto['NOMBRE'],
                'precio': str(producto['VALOR']),
                'precio_dolar': str(producto['VALOR_EN_DOLAR']),
                'cantidad': 1,
            }
        self.guardar()
    
    def guardar(self):
        self.session["carrito"] = self.carrito
        self.session.modified=True
        
    def eliminar(self, producto_id):
        producto_id = str(producto_id)
        if producto_id in self.carrito:
            del self.carrito[producto_id]
            self.guardar()
    
    def restar_producto(self, producto_id):
        producto_id = str(producto_id)
        if producto_id in self.carrito:
            self.carrito[producto_id]['cantidad'] -=1
            if self.carrito[producto_id]['cantidad'] <=0:
                self.eliminar(producto_id)
            else:
                self.guardar()
    
    def limpiar(self):
        self.session["carrito"]={}
        self.session.modified=True
    
    def obtener_total(self):
        return sum(Decimal(item['precio']) * item['cantidad'] for item in self.carrito.values())
    
    def obtener_items(self):
        return self.carrito.values()