import os
import time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def lento(texto, delay=0.012):
    for char in texto:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def logo_volcan():
    print(r"""
                          _    .  ,   .           .
                      *  / \_ *  / \_      _  *        *   /\'__        *
                        /    \  /    \,   ((        .    _/  /  \  *'.
                   .   /\/\  /\/ :' __ \_  `          _^/  ^/    `--.
                      /    \/  \  _/  \-'\      *    /.' ^_   \_   .'\  *
                    /\  .-   `. \/     \ /==~=-=~=-=-;.  _/ \ -. `_/   \
                   /  `-.__ ^   / .-'.--\ =-=~_=-=~=^/  _ `--./ .-'  `-
  ~~~~~~~~^~~^~~^~~~^~~~~^~~^~~~^~~~~^~~~~^~~~^~^~~~^~^~~~~^~^~^~~~^~^~~
            Bienvenidos a Don José – Panadería Tradicional Chapina
    """)

def marco_madera(titulo):
    print("\n" + "═" * 70)
    print(f"{titulo.center(70)}")
    print("═" * 70 + "\n")

class Panaderia:
    def __init__(self, propietario):
        self.propietario = propietario
        self.nombre_local = "Don José Panadería"
        self.ubicacion = "Antigua Guatemala"
        self.inventario = {
            "Pan Francés": {"precio": 2.00, "cantidad": 0},
            "Pan Grande": {"precio": 2.50, "cantidad": 0},
            "Tostado": {"precio": 0.25, "cantidad": 0}
        }

    def bienvenida(self):
        clear()
        logo_volcan()
        marco_madera("🌄 Bienvenido al Corazón Panadero de Antigua 🌄")
        print(f"👨‍🍳 ¡Buenos días, {self.propietario.title()}!")
        print(f"🏠 Tienda: {self.nombre_local}")
        print(f"📍 Ubicación: {self.ubicacion}")
        print("\n🥖 Que el aroma del pan fresco llene las calles coloniales...\n")

    def agregar_inventario(self):
        print("🧺 ORGANIZA TU CANASTA DEL DÍA")
        for producto in self.inventario:
            while True:
                try:
                    cantidad = int(input(f"Ingresa la cantidad para '{producto}': "))
                    self.inventario[producto]["cantidad"] = cantidad
                    break
                except ValueError:
                    lento("🚫 Por favor, ingresa un número válido.\n")

    def mostrar_inventario(self):
        print("\n📋 INVENTARIO ACTUAL")
        print("-" * 50)
        for producto, info in self.inventario.items():
            print(f"{producto:<15} | Q{info['precio']:.2f} | {info['cantidad']} disponibles")
        print("-" * 50 + "\n")

class Cliente:
    def __init__(self):
        marco_madera("👒 ¡Bienvenido a Don José Panadería! 👒")
        print("🌽 Pasa adelante, te recibimos con los brazos abiertos y pan calientito.\n")
        self.nombre = input("¿Cuál es tu nombre? ").strip().title()
        self.carrito = {}

    def bienvenida(self):
        print(f"\n🥯 {self.nombre}, mira lo que tenemos recién salido del horno:\n")

    def comprar(self, panaderia):
        total = 0

        while True:
            disponibles = [(nombre, info) for nombre, info in panaderia.inventario.items() if info["cantidad"] > 0]

            if not disponibles:
                lento("😢 Ya no nos queda pan por hoy. ¡Gracias por venir!")
                break

            if len(disponibles) == 1:
                nombre, info = disponibles[0]
                stock = info["cantidad"]
                precio = info["precio"]
                print(f"\nÚltimo producto disponible: {nombre} (Q{precio:.2f}) - {stock} unidades")
                while True:
                    desea = input("¿Deseas comprarlo? (si/no): ").strip().lower()
                    if desea not in ['si', 'no']:
                        lento("Responde con 'si' o 'no'.")
                        continue
                    break
                if desea == 'no':
                    break
                while True:
                    try:
                        cantidad = int(input(f"¿Cuántos '{nombre}' deseas?: "))
                        if cantidad > stock:
                            lento(f"Sólo tenemos {stock}.")
                            while True:
                                conf = input(f"¿Quieres los {stock}? (si/no): ").strip().lower()
                                if conf not in ['si', 'no']:
                                    lento("Por favor responde con 'si' o 'no'.")
                                    continue
                                break
                            if conf == 'si':
                                cantidad = stock
                            else:
                                break
                        if cantidad > 0:
                            self.carrito[nombre] = cantidad
                            panaderia.inventario[nombre]["cantidad"] -= cantidad
                            total += cantidad * precio
                        break
                    except ValueError:
                        lento("Ingresa un número válido.")
                break

            print("🍞 Productos disponibles:")
            for i, (nombre, info) in enumerate(disponibles, 1):
                print(f"{i}. {nombre:<15} | Q{info['precio']:.2f} | {info['cantidad']} unidades")

            try:
                seleccion = int(input("\nSelecciona el número del producto (o 0 para salir): "))
                if seleccion == 0:
                    break
                if not (1 <= seleccion <= len(disponibles)):
                    lento("Opción inválida.")
                    continue

                nombre, info = disponibles[seleccion - 1]
                stock = info["cantidad"]
                precio = info["precio"]
                cantidad = int(input(f"¿Cuántos '{nombre}' deseas?: "))

                if cantidad > stock:
                    lento(f"Sólo hay {stock}.")
                    while True:
                        aceptar = input(f"¿Deseas los {stock}? (si/no): ").strip().lower()
                        if aceptar not in ['si', 'no']:
                            lento("Responde con 'si' o 'no'.")
                            continue
                        break
                    if aceptar == 'si':
                        cantidad = stock
                    else:
                        while True:
                            otra = input("¿Quieres otro producto? (si/no): ").strip().lower()
                            if otra not in ['si', 'no']:
                                lento("Responde con 'si' o 'no'.")
                                continue
                            break
                        if otra == 'no':
                            break
                        else:
                            continue

                if cantidad > 0:
                    self.carrito[nombre] = self.carrito.get(nombre, 0) + cantidad
                    panaderia.inventario[nombre]["cantidad"] -= cantidad
                    total += cantidad * precio

            except ValueError:
                lento("Entrada inválida.")

        if self.carrito:
            marco_madera("🧾 TU CUENTA 🧾")
            for producto, cantidad in self.carrito.items():
                precio = panaderia.inventario[producto]["precio"]
                print(f"{producto} x{cantidad} → Q{cantidad * precio:.2f}")
            print(f"\n💰 TOTAL: Q{total:.2f}")
            print(f"\n🌄 Gracias por tu compra, {self.nombre}. ¡Vuelve pronto!")
        else:
            lento("No realizaste ninguna compra. ¡Te esperamos la próxima vez!")

def main():
    clear()
    logo_volcan()
    lento("🌄 Bienvenido al sistema artesanal de panadería chapina 🌽\n")
    propietario = input("¿Cuál es tu nombre, maestro panadero? ").strip().title()
    panaderia = Panaderia(propietario)
    panaderia.bienvenida()
    panaderia.agregar_inventario()

    while True:
        abrir = input("\n¿Abrimos la panadería para los clientes? (si/no): ").strip().lower()
        if abrir not in ['si', 'no']:
            lento("Responde con 'si' o 'no'.")
            continue
        if abrir == 'no':
            lento("🛑 Panadería cerrada por hoy. ¡Hasta la próxima hornada!")
            break

        cliente = Cliente()
        cliente.bienvenida()
        cliente.comprar(panaderia)
        panaderia.mostrar_inventario()

        while True:
            seguir = input("¿Deseas atender a otro cliente? (si/no): ").strip().lower()
            if seguir not in ['si', 'no']:
                lento("Responde con 'si' o 'no'.")
                continue
            break
        if seguir == 'no':
            lento("🌅 Cerrando el día con aroma a pan recién hecho... ¡Buen trabajo!")
            break

if __name__ == "__main__":
    main()
