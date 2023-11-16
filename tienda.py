import random
def bienvenida():
    mensaje = """
    ¡Bienvenid@ a "Tu Tienda Favorita"!   
    Gracias por elegir "Tu Tienda Favorita". ¡Esperamos que disfrutes de tu visita!
    """
    print(mensaje)

class RegistroCliente:
    def __init__(self):
        self.datos_cliente = {}

    def obtener_datos_cliente(self):
        print("Por favor, ingrese la siguiente información:")
        while True:
            nombre = input("Nombre: ")
            passwd = input("Contraseña: ")
            pais = input("Pais: ").lower()
            correo = input("Correo electrónico: ")
            if not nombre or not passwd or not pais or not correo:
                print("Por favor, completa todos los campos obligatorios.")
                continue
            if '@' not in correo:
                print("El correo electrónico debe contener '@'.")
                continue
            self.datos_cliente = {
                "Nombre": nombre,
                "Contraseña": passwd,
                "Pais": pais,
                "Correo electrónico": correo
            }
            break

    def mostrar_datos_cliente(self):
        print("\n¡Registro exitoso! Estos son los datos que proporcionaste:")
        for clave, valor in self.datos_cliente.items():
            print(f"{clave}: {valor}")

class ListaDeDeseos:
    def __init__(self, productos):
        self.lista_deseos = []
        self.productos = productos

    def agregar_a_lista(self, codigo_producto, cantidad=1):
        producto_seleccionado = self.productos.get(codigo_producto)
        if producto_seleccionado:
            for item in self.lista_deseos:
                if item['producto']['codigo'] == codigo_producto:
                    item['cantidad'] += cantidad
                    print(f"{cantidad} unidades de {item['producto']['nombre']} añadidas a la lista de deseos.")
                    return

            # Si el producto no está en la lista de deseos, agregarlo
            self.lista_deseos.append({'producto': producto_seleccionado, 'cantidad': cantidad})
            print(f"{cantidad} unidades de {producto_seleccionado['nombre']} añadidas a la lista de deseos.")
        else:
            print("Código de producto no válido. Por favor, selecciona un código válido.")

    def mostrar_productos_disponibles(self):
        print("Productos Disponibles:")
        for codigo, producto_info in self.productos.items():
            print(f"Código {codigo}: {producto_info['nombre']} - Precio: ${producto_info['precio']} - Unidades disponibles: {producto_info['unidades']}")

    def simular_agregar_a_lista(self):
        # Simular que el cliente agrega productos a la lista de deseos
        while True:
            try:
                codigo_seleccionado = int(input("\nSelecciona un producto ingresando su código (o 0 para salir): "))
                if codigo_seleccionado == 0:
                    break

                if codigo_seleccionado in self.productos:
                    cantidad_seleccionada = int(input(f"¿Cuántas unidades de {self.productos[codigo_seleccionado]['nombre']} deseas agregar? "))
                    self.agregar_a_lista(codigo_seleccionado, cantidad_seleccionada)
                else:
                    print("Código no válido. Por favor, selecciona un código válido.")
            except ValueError:
                print("Ingresa un número válido.")

    def mostrar_lista(self):
        if not self.lista_deseos:
            print("Tu lista de deseos está vacía.")
        else:
            print("Tu lista de deseos:")
            for item in self.lista_deseos:
                print(f"{item['cantidad']} unidades de {item['producto']['nombre']}")

# Definir productos
productos = {
    1: {"nombre": "Camiseta", "precio": 19.99, "unidades": 50, "codigo": 1},
    2: {"nombre": "Zapatos", "precio": 49.99, "unidades": 30, "codigo": 2},
    3: {"nombre": "Reloj", "precio": 99.99, "unidades": 20, "codigo": 3},
    4: {"nombre": "Libro", "precio": 9.99, "unidades": 100, "codigo": 4},
    5: {"nombre": "Cámara", "precio": 199.99, "unidades": 15, "codigo": 5},
    6: {"nombre": "Auriculares", "precio": 39.99, "unidades": 40, "codigo": 6},
    7: {"nombre": "Teclado", "precio": 29.99, "unidades": 25, "codigo": 7},
    8: {"nombre": "Mouse", "precio": 19.49, "unidades": 35, "codigo": 8},
    9: {"nombre": "Silla", "precio": 79.99, "unidades": 10, "codigo": 9},
    10: {"nombre": "Mesa", "precio": 129.99, "unidades": 15, "codigo": 10},
    11: {"nombre": "Lámpara", "precio": 24.99, "unidades": 30, "codigo": 11},
    12: {"nombre": "Bolso", "precio": 34.99, "unidades": 20, "codigo": 12}
}

class MetodoDePago:
    def __init__(self, paises_iva):
        self.paises_iva = paises_iva

    def obtener_iva(self, pais):
        return self.paises_iva.get(pais, 0.21)

    def procesar_pago(self, lista_deseos, pais_cliente):
        iva = self.obtener_iva(pais_cliente)

        total = 0
        for item in lista_deseos:
            precio_unitario = item['producto']['precio']
            cantidad = item['cantidad']
            subtotal = precio_unitario * cantidad
            total += subtotal

        total_con_iva = total * (1 + iva)
        print(f"\nTotal de la compra con IVA ({iva * 100}%): ${total_con_iva:.2f}")
        print("¡Gracias por tu compra!")
        print("Se le ha enviado un correo con un PDF con la factura de su pedido.")

# Lista de países con sus respectivos IVAs
paises_iva = {
    "España": 0.21,
    "Alemania": 0.15,
    "Belgica": 0.05,
    "Francia": 0.18,
}

class SeguimientoPaquetes:
    def __init__(self):
        self.codigo_seguimiento = None

    def generar_codigo_seguimiento(self):
        return ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(10))

    def solicitar_seguimiento(self):
        respuesta = input("¿Desea obtener un código de seguimiento para su paquete? (Sí/No): ").lower()

        if respuesta == 'si':
            self.codigo_seguimiento = self.generar_codigo_seguimiento()
            print(f"\nGracias por su compra. Su código de seguimiento es: {self.codigo_seguimiento}")
        elif respuesta == 'no':
            print("\nGracias por su compra. No se proporcionará un código de seguimiento.")
        else:
            print("\nRespuesta no válida. Por favor, responda con 'Sí' o 'No'.")



