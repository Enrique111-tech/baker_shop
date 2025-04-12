class Panaderia:
    def __init__(self, name, location, products, budget):
        self.name = name
        self.location = location
        self.products = products  # Diccionario con productos y precios {'pan': 10, 'pastel': 50}
        self.budget = budget
        self.new_store = []
        self.clientes = []  # Lista de clientes con deudas

    def products_available(self):
        return self.products

    def saves(self):
        return self.budget

    def new_store(self, name, location, budget):
        nueva_panaderia = Panaderia(name, location, {}, budget)
        self.new_store.append(nueva_panaderia)
        return nueva_panaderia

    def registrar_cliente(self, cliente):
        self.clientes.append(cliente)

    def __repr__(self):
        return f"Panadería '{self.name}' ubicada en {self.location}, presupuesto: {self.budget}"


class Cliente:
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget
        self.total = 0
        self.deuda = 0  # Deuda del cliente

    def comprar(self, panaderia, producto, cantidad):
        if producto in panaderia.products:
            precio_total = panaderia.products[producto] * cantidad
            if self.budget >= precio_total:
                self.budget -= precio_total
                panaderia.budget += precio_total
                self.total += precio_total
                print(f"{self.name} compró {cantidad} {producto}(s) por {precio_total}.")
            else:
                self.deuda += precio_total
                panaderia.budget += precio_total
                panaderia.registrar_cliente(self)
                print(f"{self.name} no tiene suficiente presupuesto. Se agregó una deuda de {precio_total}.")
        else:
            print(f"El producto '{producto}' no está disponible en la panadería.")

    def __repr__(self):
        return f"Cliente '{self.name}', presupuesto: {self.budget}, deuda: {self.deuda}"


# Arte ASCII para la bienvenida
print(r"""
  ██████╗  █████╗ ███╗   ██╗ █████╗ ██████╗ ███████╗██╗ █████╗ 
 ██╔════╝ ██╔══██╗████╗  ██║██╔══██╗██╔══██╗██╔════╝██║██╔══██╗
 ██║  ███╗███████║██╔██╗ ██║███████║██║  ██║█████╗  ██║███████║
 ██║   ██║██╔══██║██║╚██╗██║██╔══██║██║  ██║██╔══╝  ██║██╔══██║
 ╚██████╔╝██║  ██║██║ ╚████║██║  ██║██████╔╝███████╗██║██║  ██║
  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝╚═╝  ╚═╝
""")
print("¡Bienvenido a la Panadería!")

# Crear instancias de Panadería y Cliente
panaderia1 = Panaderia("Panadería Central", "Centro", {"pan": 10, "pastel": 50, "galleta": 5}, 50000)
cliente1 = Cliente("Juan", 100)
cliente2 = Cliente("Maria", 30)

# Interacciones entre las clases
cliente1.comprar(panaderia1, "pan", 5)  # Compra exitosa
cliente2.comprar(panaderia1, "pastel", 1)  # Compra con deuda

# Verificar si la panadería puede abrir una nueva sucursal
if panaderia1.saves() > 100000:
    nueva_panaderia = panaderia1.new_store("Panadería Norte", "Norte", 30000)
    print(f"Se abrió una nueva panadería: {nueva_panaderia}")

# Mostrar información de la panadería y los clientes
print(panaderia1)
print(cliente1)
print(cliente2)

# Mostrar lista de clientes con deudas
print("Clientes con deudas:")
for cliente in panaderia1.clientes:
    print(cliente)