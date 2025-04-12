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
        print("="*50)
        print("🍞 BIENVENIDO A LA PANADERÍA DON JOSÉ 🍞".center(50))
        print("="*50)
        print(f"\nBuenos días {self.propietario}, propietario de la panadería {self.nombre_local}, ubicada en {self.ubicacion}.\n")

    def agregar_inventario(self):
        print("Vamos a registrar la cantidad de productos disponibles:\n")
        for producto in self.inventario:
            while True:
                try:
                    cantidad = int(input(f"Ingrese la cantidad para '{producto.title()}': "))
                    self.inventario[producto]["cantidad"] = cantidad
                    break
                except ValueError:
                    print("Por favor, ingrese un número válido.")


class Cliente:
    def __init__(self):
        self.nombre = input("Ingresa tu nombre: ").strip()
        self.carrito = {}

    def bienvenida(self):
        print("""
  _______              _                _           
 |__   __|            | |              | |          
    | | __ _ _ __   __| | ___  ___  ___| |__   __ _ 
    | |/ _` | '_ \\ / _` |/ _ \\/ __|/ __| '_ \\ / _` |
    | | (_| | | | | (_| |  __/\\__ \\ (__| | | | (_| |
    |_|\\__,_|_| |_|\\__,_|\\___||___/\\___|_| |_|\\__,_|

        """)
        print(f"¡Bienvenido {self.nombre}!")

    def comprar(self, panaderia):
        total = 0

        while True:
            productos_disponibles = [
                (nombre, datos) for nombre, datos in panaderia.inventario.items()
                if datos["cantidad"] > 0
            ]

            if not productos_disponibles:
                print("❌ Lo sentimos, no hay productos disponibles en este momento.")
                break

            if len(productos_disponibles) == 1:
                nombre_producto, datos = productos_disponibles[0]
                print(f"\n🔸 Solo queda un producto disponible: '{nombre_producto.title()}' - Q{datos['precio']:.2f} ({datos['cantidad']} disponibles)")
                while True:
                    desea = input("¿Deseas comprar este producto? (si/no): ").strip().lower()
                    if desea not in ['si', 'no']:
                        print("⚠️ Por favor escribe 'si' o 'no' para continuar.")
                        continue
                    break
                if desea == 'si':
                    while True:
                        try:
                            cantidad = int(input(f"¿Cuántos '{nombre_producto}' deseas?: "))
                            stock = datos['cantidad']
                            precio = datos['precio']

                            if cantidad > stock:
                                print(f"\n⚠️ Solo hay {stock} unidades disponibles.")
                                while True:
                                    aceptar = input(f"¿Deseas comprar esas {stock} unidades? (si/no): ").strip().lower()
                                    if aceptar not in ['si', 'no']:
                                        print("⚠️ Por favor escribe 'si' o 'no' para continuar.")
                                        continue
                                    break
                                if aceptar == 'si':
                                    cantidad = stock
                                else:
                                    break

                            if cantidad > 0:
                                self.carrito[nombre_producto] = self.carrito.get(nombre_producto, 0) + cantidad
                                panaderia.inventario[nombre_producto]["cantidad"] -= cantidad
                                total += cantidad * precio
                                print(f"✔️ {cantidad} '{nombre_producto}' añadidos al carrito.")
                        except ValueError:
                            print("❗ Entrada no válida.")
                else:
                    print("Compra finalizada.")
                break

            print("\n¿Qué producto deseas comprar?")
            for i, (nombre, datos) in enumerate(productos_disponibles, 1):
                print(f"{i}. {nombre.title():<15} - Q{datos['precio']:.2f} ({datos['cantidad']} disponibles)")

            try:
                seleccion = int(input("Selecciona una opción (1-{0}) o 0 para terminar: ".format(len(productos_disponibles))))
                if seleccion == 0:
                    break
                if seleccion < 1 or seleccion > len(productos_disponibles):
                    print("❗ Selección inválida. Intenta de nuevo.")
                    continue

                nombre_producto, datos = productos_disponibles[seleccion - 1]
                stock = datos['cantidad']
                precio = datos['precio']

                cantidad = int(input(f"¿Cuántos '{nombre_producto}' deseas?: "))

                if cantidad > stock:
                    print(f"\n⚠️ Solo tenemos {stock} unidades de '{nombre_producto}'.")
                    while True:
                        aceptar = input(f"¿Deseas comprar esas {stock} unidades? (si/no): ").strip().lower()
                        if aceptar not in ['si', 'no']:
                            print("⚠️ Por favor escribe 'si' o 'no' para continuar.")
                            continue
                        break
                    if aceptar == 'si':
                        cantidad = stock
                    else:
                        while True:
                            otro = input("¿Deseas intentar con otro producto? (si/no): ").strip().lower()
                            if otro not in ['si', 'no']:
                                print("⚠️ Por favor escribe 'si' o 'no' para continuar.")
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
                    print(f"✔️ {cantidad} '{nombre_producto}' añadidos - Subtotal: Q{subtotal:.2f}")
            except ValueError:
                print("❗ Entrada no válida. Intenta de nuevo.")

        if self.carrito:
            print("\n🧾 Resumen de compra:")
            for prod, cant in self.carrito.items():
                precio_unitario = panaderia.inventario[prod]["precio"]
                print(f"{prod.title():<15} x{cant:<3} - Q{cant * precio_unitario:.2f}")

            print(f"\n💵 Total a pagar: Q{total:.2f}")
            print(f"\nGracias por tu compra, {self.nombre}! ¡Vuelve pronto!\n")
        else:
            print("\nNo se realizaron compras. ¡Hasta la próxima!\n")


def main():
    propietario = input("Ingrese su nombre como propietario de la panadería: ").strip()
    panaderia = Panaderia(propietario)
    panaderia.bienvenida()
    panaderia.agregar_inventario()

    while True:
        abrir = input("¿Deseas abrir la panadería para atender clientes? (si/no): ").strip().lower()
        if abrir not in ["si", "no"]:
            print("⚠️ Por favor, escribe 'si' o 'no' para continuar.")
            continue
        elif abrir == "no":
            print("Panadería cerrada. ¡Hasta luego!")
            break
        else:
            cliente = Cliente()
            cliente.bienvenida()
            cliente.comprar(panaderia)


if __name__ == "__main__":
    main()
