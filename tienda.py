import random
from colorama import Fore, Style
from tabulate import tabulate
def bienvenida():
    mensaje = """
    ¡Bienvenid@ a Adrian's Elegance Emporium!   
    ¡Esperamos que disfrutes de tu visita!
    """
    print(mensaje)

class RegistroCliente:
    def __init__(self):
        self.datos_cliente = {}

    def iniciar_registro(self):
        respuesta = input(
            f"{Fore.GREEN}¿Deseas iniciar tu registro en 'Tu Tienda Favorita'? (Sí/No): {Style.RESET_ALL}").lower()
        if respuesta != 'si':
            print(f"{Fore.RED}¡Gracias por visitarnos! Hasta luego.{Style.RESET_ALL}")
            exit()

    def obtener_datos_cliente(self):
        print(f"{Fore.MAGENTA}Vamos a comenzar el registro, ingrese la siguiente información:{Style.RESET_ALL}")
        while True:
            nombre = input(f"{Fore.GREEN}Nombre:{Style.RESET_ALL} ")
            passwd = input(f"{Fore.GREEN}Contraseña:{Style.RESET_ALL} ")
            print(f"{Fore.BLUE}Paises que importamos:\n 1.España, 2.Alemania, 3.Belgica, 4.Francia{Style.RESET_ALL}")
            pais = input(f"{Fore.GREEN}Pais:{Style.RESET_ALL} ").lower()
            if not nombre or not passwd or not pais:
                print(f"{Fore.RED}Por favor, completa todos los campos obligatorios.{Style.RESET_ALL}")
                continue
            self.datos_cliente = {
                "Nombre": nombre,
                "Contraseña": passwd,
                "Pais": pais,
            }
            break
    def mostrar_datos_cliente(self):
        print(f"{Fore.GREEN}\n¡Registro exitoso! Estos son los datos que proporcionaste:{Style.RESET_ALL}")
        for clave, valor in self.datos_cliente.items():
            print(f"{clave}: {valor}")


class ListaDeDeseos:
    def __init__(self, productos):
        self.lista_deseos = []
        self.productos = productos.copy()
        self.productos_originales = productos.copy()

    def agregar_a_lista(self, codigo_producto, cantidad=1):
        producto_seleccionado = self.productos.get(codigo_producto)
        if producto_seleccionado:
            for item in self.lista_deseos:
                if item['producto']['codigo'] == codigo_producto:
                    item['cantidad'] += cantidad
                    print(f"{cantidad} unidades de {item['producto']['nombre']} añadidas a la lista de deseos.")
                    self.productos[codigo_producto]['unidades'] -= cantidad
                    return

            self.lista_deseos.append({'producto': producto_seleccionado, 'cantidad': cantidad})
            print(f"{cantidad} unidades de {producto_seleccionado['nombre']} añadidas a la lista de deseos.")
            self.productos[codigo_producto]['unidades'] -= cantidad
        else:
            print(f"{Fore.RED}Código de producto no válido. Por favor, selecciona un código válido.{Style.RESET_ALL}")

    def mostrar_productos_disponibles(self):
        productos_tabla = []
        for codigo, producto_info in self.productos.items():
            productos_tabla.append([codigo, producto_info['nombre'], f"${producto_info['precio']}", producto_info['unidades']])

        headers = [f"{Fore.BLUE}Código{Style.RESET_ALL}", f"{Fore.BLUE}Nombre{Style.RESET_ALL}", f"{Fore.BLUE}Precio{Style.RESET_ALL}", f"{Fore.BLUE}Unidades{Style.RESET_ALL}"]
        print(tabulate(productos_tabla, headers=headers, tablefmt="fancy_grid"))

    def simular_agregar_a_lista(self):
        while True:
            try:
                codigo_seleccionado = int(input(f"{Fore.MAGENTA}\nSelecciona un producto ingresando su código (o 0 para salir):{Style.RESET_ALL} "))
                if codigo_seleccionado == 0:
                    break

                if codigo_seleccionado in self.productos:
                    cantidad_seleccionada = int(input(f"{Fore.MAGENTA}¿Cuántas unidades de {self.productos[codigo_seleccionado]['nombre']} deseas agregar?{Style.RESET_ALL} "))
                    self.agregar_a_lista(codigo_seleccionado, cantidad_seleccionada)
                else:
                    print(f"{Fore.RED}Código no válido. Por favor, selecciona un código válido.{Style.RESET_ALL}")
            except ValueError:
                print(f"{Fore.RED}Ingresa un número válido.{Style.RESET_ALL}")

    def mostrar_lista(self):
        if not self.lista_deseos:
            print(f"{Fore.RED}Tu lista de deseos está vacía.{Style.RESET_ALL}")
        else:
            print(f"{Fore.BLUE}Tu lista de deseos:{Style.RESET_ALL}")
            for item in self.lista_deseos:
                print(f"{Fore.MAGENTA}{item['cantidad']} unidades de {item['producto']['nombre']}{Style.RESET_ALL}")

    def restaurar_productos_originales(self):
        self.productos = self.productos_originales.copy()

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

    def obtener_correo_valido(self):
        while True:
            correo_cliente = input(f"{Fore.GREEN}Por favor, ingrese su correo electrónico para enviar la factura: {Style.RESET_ALL}")
            if '@' in correo_cliente and '.' in correo_cliente:
                return correo_cliente
            else:
                print(f"{Fore.RED}El correo electrónico debe contener al menos un '@' y al menos un '.'{Style.RESET_ALL}")

    def procesar_pago(self, lista_deseos, pais_cliente):
        iva = self.obtener_iva(pais_cliente)

        total = 0
        for item in lista_deseos:
            precio_unitario = item['producto']['precio']
            cantidad = item['cantidad']
            subtotal = precio_unitario * cantidad
            total += subtotal

        total_con_iva = total * (1 + iva)
        correo_cliente = self.obtener_correo_valido()
        print(f"{Fore.MAGENTA}\nTotal de la compra con IVA ({iva * 100}%): €{total_con_iva:.2f}{Style.RESET_ALL}")
        print(f"{Fore.BLUE}¡Gracias por tu compra! Se le ha enviado un correo a {correo_cliente} con un PDF con la factura de su pedido.{Style.RESET_ALL}")

paises_iva = {
    "1": 0.21,
    "2": 0.15,
    "3": 0.05,
    "4": 0.18,
}

class SeguimientoPaquetes:
    def __init__(self):
        self.codigo_seguimiento = None

    def generar_codigo_seguimiento(self):
        return ''.join(random.choice(f'{Fore.GREEN}ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789{Style.RESET_ALL}') for _ in range(10))

    def obtener_telefono_valido(self):
        while True:
            telefono_cliente = input(f"{Fore.GREEN}Por favor, ingrese su número de teléfono para recibir el código de seguimiento: {Style.RESET_ALL}")
            if telefono_cliente.isdigit() and len(telefono_cliente) >= 9:
                return telefono_cliente
            else:
                print(f"{Fore.RED}Número de teléfono no válido. Asegúrese de ingresar un número con al menos 9 dígitos.{Style.RESET_ALL}")

    def solicitar_seguimiento(self):
        respuesta = input("¿Desea obtener un código de seguimiento para su paquete? (Sí/No): ").lower()

        if respuesta == 'si':
            self.codigo_seguimiento = self.generar_codigo_seguimiento()
            telefono_cliente = self.obtener_telefono_valido()
            print(f"{Fore.GREEN}\nGracias por su compra. Su código de seguimiento se ha enviado a su número de teléfono: {telefono_cliente}.{Style.RESET_ALL}")
        elif respuesta == 'no':
            print(f"{Fore.GREEN}\nGracias por su compra. No se proporcionará un código de seguimiento.{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}\nRespuesta no válida. Por favor, responda con 'Sí' o 'No'.{Style.RESET_ALL}")




