import os
import time

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def escribir_lento(texto, delay=0.03):
    for letra in texto:
        print(letra, end='', flush=True)
        time.sleep(delay)
    print()

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
        limpiar_pantalla()
        encabezado = r"""
===============================================
||       ██████╗  █████╗ ███╗   ██╗          ||
||      ██╔════╝ ██╔══██╗████╗  ██║          ||
||      ██║  ███╗███████║██╔██╗ ██║          ||
||      ██║   ██║██╔══██║██║╚██╗██║          ||
||      ╚██████╔╝██║  ██║██║ ╚████║          ||
||       ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝          ||
||                                           ||
||      Bienvenid@ a la Panadería Retro      ||
===============================================
"""
        print(encabezado)
        escribir_lento(f"Buenos días, {self.propietario}.")
        escribir_lento(f"Eres el orgulloso propietario de la panadería '{self.nombre_tienda}',")
        escribir_lento(f"ubicada en la hermosa ciudad de {self.ubicacion}.\n")

    def agregar_productos(self):
        print("Por favor ingresa la cantidad de productos que tienes en inventario:\n")
        for producto in self.inventario:
            while True:
                try:
                    cantidad = int(input(f"Ingrese la cantidad de '{producto}': "))
                    self.inventario[producto]["cantidad"] = cantidad
                    break
                except ValueError:
                    print("❗ Por favor ingresa un número válido.")
        print("\n✅ Inventario actualizado con éxito.\n")

    def mostrar_inventario(self):
        print("\n🧺 Inventario actual:")
        print("-" * 40)
        for producto, datos in self.inventario.items():
            print(f"{producto.title():<20} | {datos['cantidad']} unidades | Q{datos['precio']:.2f}")
        print("-" * 40)


class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.carrito = {}

    def bienvenida(self):
        limpiar_pantalla()
        logo = r"""
    ==========================
    ||     __    _          ||
    ||    / /   (_)___ ___  ||
    ||   / /   / / __ `__ \ ||
    ||  / /___/ / / / / / / ||
    || /_____/_/_/ /_/ /_/  ||
    ||                     ||
    ||  Pan caliente del día ||
    ==========================
        """
        print(logo)
        escribir_lento(f"\nHola, {self.nombre}, bienvenido a la panadería Don José 🥖\n")

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
                desea = input("¿Deseas comprar este producto? (s/n): ").strip().lower()
                if desea == 's':
                    try:
                        cantidad = int(input(f"¿Cuántos '{nombre_producto}' deseas?: "))
                        stock = datos['cantidad']
                        precio = datos['precio']

                        if cantidad > stock:
                            print(f"\n⚠️ Solo hay {stock} unidades disponibles.")
                            aceptar = input(f"¿Deseas comprar esas {stock} unidades? (s/n): ").strip().lower()
                            if aceptar == 's':
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
                    aceptar = input(f"¿Deseas comprar esas {stock} unidades? (s/n): ").strip().lower()
                    if aceptar == 's':
                        cantidad = stock
                    else:
                        otro = input("¿Deseas intentar con otro producto? (s/n): ").strip().lower()
                        if otro != 's':
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


# PROGRAMA PRINCIPAL
def main():
    limpiar_pantalla()
    print("\n=========== SISTEMA DE PANADERÍA ===========\n")
    propietario = input("Ingrese su nombre como propietario de la panadería: ")
    tienda = Panaderia(propietario)
    tienda.bienvenida()
    tienda.agregar_productos()
    tienda.mostrar_inventario()

    while True:
        respuesta = input("\n¿Deseas atender a un cliente? (si/no): ").strip().lower()
        if respuesta not in ['si', 'no']:
            print("⚠️ Por favor, responde únicamente con 'si' o 'no'.")
            continue
        if respuesta == 'no':
            print("\nCerrando la panadería... ¡Hasta mañana!\n")
            break
        nombre_cliente = input("Ingrese el nombre del cliente: ")
        cliente = Cliente(nombre_cliente)
        cliente.bienvenida()
        cliente.comprar(tienda)
        tienda.mostrar_inventario()

if __name__ == "__main__":
    main()
