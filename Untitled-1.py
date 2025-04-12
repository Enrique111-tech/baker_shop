class Panaderia:
    def __init__(self, propietario):
        self.nombre_local = "Don José"
        self.ubicacion = "Antigua Guatemala"
        self.propietario = propietario
        self.inventario = {
            "pan frances": {"precio": 2.00, "cantidad": 0},
            "pan grande": {"precio": 2.50, "cantidad": 0},
            "tostado": {"precio": 0.25, "cantidad": 0}
        }

    def bienvenida(self):
        print("\n" + "="*60)
        print("|{:^58}|".format("= BIENVENIDO A LA PANADERÍA ="))
        print("="*60)
        print(f"| Propietario: {self.propietario:<44}|")
        print(f"| Nombre del local: {self.nombre_local:<40}|")
        print(f"| Ubicación: {self.ubicacion:<45}|")
        print("="*60 + "\n")

    def agregar_inventario(self):
        print("Ingrese la cantidad inicial de productos:\n")
        for producto in self.inventario:
            while True:
                try:
                    cantidad = int(input(f"Cantidad de '{producto.title()}': "))
                    self.inventario[producto]["cantidad"] = cantidad
                    break
                except ValueError:
                    print("Ingrese un número válido.")


class Cliente:
    def __init__(self):
        print("\n" + "#"*50)
        print("#{:^48}#".format("🧺 PANADERÍA DON JOSÉ 🧺"))
        print("#"*50)
        self.nombre = input("Nombre del cliente: ").strip()
        self.carrito = {}

    def bienvenida(self):
        print("\n" + "-"*50)
        print(f"Hola {self.nombre}, bienvenido a la panadería Don José.")
        print("Tenemos pan fresquito recién salido del horno!")
        print("-"*50)

    def comprar(self, panaderia):
        total = 0

        while True:
            productos_disponibles = [
                (nombre, datos) for nombre, datos in panaderia.inventario.items()
                if datos["cantidad"] > 0
            ]

            if not productos_disponibles:
                print("No hay productos disponibles en este momento.")
                break

            if len(productos_disponibles) == 1:
                nombre_producto, datos = productos_disponibles[0]
                stock = datos["cantidad"]
                precio = datos["precio"]

                print(f"\nÚltimo producto disponible: '{nombre_producto.title()}'")
                print(f"Precio: Q{precio:.2f} - Stock: {stock}")
                while True:
                    desea = input(f"¿Deseas comprar '{nombre_producto}'? (si/no): ").strip().lower()
                    if desea not in ['si', 'no']:
                        print("Por favor escribe 'si' o 'no'.")
                        continue
                    break

                if desea == 'no':
                    print("Compra finalizada.")
                    break

                while True:
                    try:
                        cantidad = int(input(f"¿Cuántos '{nombre_producto}' deseas?: "))
                        if cantidad > stock:
                            print(f"Sólo tenemos {stock}.")
                            while True:
                                aceptar = input(f"¿Deseas comprar {stock}? (si/no): ").strip().lower()
                                if aceptar not in ['si', 'no']:
                                    print("Por favor escribe 'si' o 'no'.")
                                    continue
                                break
                            if aceptar == 'si':
                                cantidad = stock
                            else:
                                print("Compra finalizada.")
                                break
                        if cantidad > 0:
                            self.carrito[nombre_producto] = cantidad
                            panaderia.inventario[nombre_producto]["cantidad"] -= cantidad
                            total += cantidad * precio
                            print(f"{cantidad} '{nombre_producto}' añadidos.")
                        break
                    except ValueError:
                        print("Ingresa un número válido.")
                # No volver a ofrecer nada más aunque quede en stock
                break

            print("\nProductos disponibles:")
            for i, (nombre, datos) in enumerate(productos_disponibles, 1):
                print(f"{i}. {nombre.title()} - Q{datos['precio']:.2f} ({datos['cantidad']} disponibles)")

            try:
                seleccion = int(input(f"\nSelecciona un producto (1-{len(productos_disponibles)}) o 0 para terminar: "))
                if seleccion == 0:
                    break
                if not 1 <= seleccion <= len(productos_disponibles):
                    print("Opción inválida.")
                    continue

                nombre_producto, datos = productos_disponibles[seleccion - 1]
                stock = datos["cantidad"]
                precio = datos["precio"]

                cantidad = int(input(f"¿Cuántos '{nombre_producto}' deseas?: "))

                if cantidad > stock:
                    print(f"Sólo tenemos {stock} unidades.")
                    while True:
                        aceptar = input(f"¿Deseas comprar {stock}? (si/no): ").strip().lower()
                        if aceptar not in ['si', 'no']:
                            print("Por favor escribe 'si' o 'no'.")
                            continue
                        break
                    if aceptar == 'si':
                        cantidad = stock
                    else:
                        while True:
                            otro = input("¿Deseas intentar con otro producto? (si/no): ").strip().lower()
                            if otro not in ['si', 'no']:
                                print("Por favor escribe 'si' o 'no'.")
                                continue
                            break
                        if otro == 'no':
                            break
                        else:
                            continue

                if cantidad > 0:
                    self.carrito[nombre_producto] = self.carrito.get(nombre_producto, 0) + cantidad
                    panaderia.inventario[nombre_producto]["cantidad"] -= cantidad
                    subtotal = cantidad * precio
                    total += subtotal
                    print(f"{cantidad} '{nombre_producto}' añadidos - Subtotal: Q{subtotal:.2f}")
            except ValueError:
                print("Entrada inválida.")

        if self.carrito:
            print("\n" + "="*50)
            print(f"Resumen de compra de {self.nombre}:")
            for prod, cant in self.carrito.items():
                precio_unitario = panaderia.inventario[prod]["precio"]
                print(f"- {prod.title()} x{cant} = Q{cant * precio_unitario:.2f}")
            print(f"\nTotal a pagar: Q{total:.2f}")
            print("="*50)
            print(f"¡Gracias por tu compra, {self.nombre}! Hasta pronto.\n")
        else:
            print("\nNo realizaste ninguna compra. ¡Vuelve pronto!\n")


def main():
    propietario = input("Ingrese el nombre del propietario: ").strip()
    panaderia = Panaderia(propietario)
    panaderia.bienvenida()
    panaderia.agregar_inventario()

    while True:
        abrir = input("¿Deseas abrir la panadería para clientes? (si/no): ").strip().lower()
        if abrir not in ['si', 'no']:
            print("Por favor, escribe 'si' o 'no'.")
            continue
        if abrir == 'no':
            print("Panadería cerrada. ¡Hasta la próxima!")
            break
        cliente = Cliente()
        cliente.bienvenida()
        cliente.comprar(panaderia)


if __name__ == "__main__":
    main()
