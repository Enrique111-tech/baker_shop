# panaderia.py

class Panaderia:
    def __init__(self, propietario):
        self.propietario = propietario
        self.nombre_tienda = "Don José"
        self.ubicacion = "Antigua Guatemala"
        self.inventario = {
            "pan francés": {"precio": 2.00, "cantidad": 0},
            "pan grande": {"precio": 2.50, "cantidad": 0},
            "tostado": {"precio": 0.25, "cantidad": 0}
        }

    def bienvenida(self):
        print(f"\nBuenos días {self.propietario}, propietario de la panadería '{self.nombre_tienda}', ubicada en {self.ubicacion}.\n")

    def agregar_productos(self):
        print("Por favor ingrese la cantidad de productos que tiene en inventario:")
        for producto in self.inventario:
            cantidad = int(input(f"Ingrese la cantidad de '{producto}': "))
            self.inventario[producto]["cantidad"] = cantidad
        print("\nInventario actualizado con éxito.\n")

    def mostrar_inventario(self):
        print("Inventario actual:")
        for producto, datos in self.inventario.items():
            print(f"{producto.title()}: {datos['cantidad']} unidades disponibles - Q{datos['precio']:.2f}")


class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.carrito = {}

    def bienvenida(self):
        logo = r"""
         ______
        /      \\
       |  PAN   |
       |_______ |
        ( ) ( )
        """
        print(logo)
        print(f"\n¡Bienvenido a la panadería, {self.nombre}!\n")

    def comprar(self, panaderia):
        print("Lista de productos disponibles:")
        for producto, datos in panaderia.inventario.items():
            print(f"{producto.title()}: Q{datos['precio']:.2f} - {datos['cantidad']} disponibles")

        while True:
            producto = input("\n¿Qué producto desea comprar? (escriba 'salir' para terminar): ").strip().lower()
            if producto == 'salir':
                break
            if producto in panaderia.inventario:
                cantidad = int(input(f"¿Cuántos '{producto}' desea comprar?: "))
                if cantidad <= panaderia.inventario[producto]["cantidad"]:
                    self.carrito[producto] = self.carrito.get(producto, 0) + cantidad
                    panaderia.inventario[producto]["cantidad"] -= cantidad
                    print(f"{cantidad} unidades de '{producto}' agregadas al carrito.")
                else:
                    print("Lo siento, no hay suficiente cantidad en inventario.")
            else:
                print("Producto no válido.")

        print(f"\nGracias por su compra, {self.nombre}!\n")


# PROGRAMA PRINCIPAL
def main():
    propietario = input("Ingrese su nombre como propietario de la panadería: ")
    tienda = Panaderia(propietario)
    tienda.bienvenida()
    tienda.agregar_productos()
    tienda.mostrar_inventario()

    while True:
        respuesta = input("\n¿Desea atender a un cliente? (s/n): ").strip().lower()
        if respuesta != 's':
            print("Cerrando la panadería. ¡Buen trabajo!")
            break
        nombre_cliente = input("Ingrese el nombre del cliente: ")
        cliente = Cliente(nombre_cliente)
        cliente.bienvenida()
        cliente.comprar(tienda)
        tienda.mostrar_inventario()


if __name__ == "__main__":
    main()
