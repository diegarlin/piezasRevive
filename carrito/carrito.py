from decimal import Decimal
from producto.models import Producto

class Carrito:
    def __init__(self, request):
        self.request=request
        self.session=request.session
        carrito=self.session.get("carrito")
        if not carrito:
            carrito=self.session["carrito"]={}
        #else:
        self.carrito=carrito

    def agregar(self, producto):
        if not 'cantidad' in self.request.GET or self.request.GET['cantidad'] == '':
            cantidad = 1
        else:
            cantidad = abs(int(self.request.GET['cantidad']))

        if(str(producto.id) not in self.carrito.keys()):
            self.carrito[producto.id]={
                "producto_id":producto.id,
                "nombre":producto.nombre,
                "categoria":producto.categoria,
                "marca":producto.marca,
                "descripcion":producto.descripcion,
                "precio": str(producto.precio*cantidad),
                "cantidad":cantidad,
                "imagen":producto.imagen,
                "stock":producto.stock
            }
        else:
            for key, value in self.carrito.items():
                if key==str(producto.id):
                    value["cantidad"]=value["cantidad"]+cantidad
                    value["precio"]=float(value["precio"])+producto.precio*cantidad
                    break
        self.guardar_carrito()

    def restar(self, producto):
        if not 'cantidad' in self.request.GET or self.request.GET['cantidad'] == '':
            cantidad = 1
        else:
            cantidad = abs(int(self.request.GET['cantidad']))

        for key, value in self.carrito.items():
                if key==str(producto.id):
                    value["cantidad"]=value["cantidad"]-cantidad
                    value["precio"]=float(value["precio"])-producto.precio*cantidad
                    if value["cantidad"]<1:
                        self.eliminar(producto)
                    break
        self.guardar_carrito()

    def precio_total(self):
        return sum(float(value['precio']) for value in self.carrito.values())
    
    def gastos_envio(self):
        if self.precio_total() < 1000:
            return 8.47
        else:
            return 0
        
    def precio_final(self):
        if self.precio_total() == 0:
            return 0
        else:
            return self.precio_total() + self.gastos_envio()

    def guardar_carrito(self):
        self.session["carrito"]=self.carrito
        self.session.modified=True


    def eliminar(self, producto):
        producto.id=str(producto.id)
        if producto.id in self.carrito:
            del self.carrito[producto.id]
            self.guardar_carrito()

    def limpiar_carrito(self):
        self.session["carrito"]={}
        self.session.modified=True


        
