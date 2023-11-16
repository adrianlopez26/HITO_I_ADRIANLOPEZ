import tienda as t
from colorama import Fore, Style
import pyfiglet

def imprimir_titulo_bonito(titulo):
    ascii_art = pyfiglet.figlet_format(titulo, font="big", width=150)
    print(f"{Fore.BLUE}{ascii_art.rstrip()}{Style.RESET_ALL}", end='')

titulo_bienvenida = "¡Adrian's Elegance Emporium!"
imprimir_titulo_bonito(titulo_bienvenida)

def preguntar_opcion():
    while True:
        opcion = input(f"{Fore.BLUE}\n¿Qué deseas hacer? (1.Continuar/2.Volver/3.Salir):{Style.RESET_ALL} ").lower()
        if opcion in ['1', '2', '3']:
            return opcion
        else:
            print("Opción no válida. Por favor, elige entre '1.Continuar', '2.Volver' o '3.Salir'.")
if __name__ == '__main__':
    t.bienvenida()
    registro = t.RegistroCliente()
    registro.iniciar_registro()
    registro.obtener_datos_cliente()
    registro.mostrar_datos_cliente()
    while True:
        opcion = preguntar_opcion()
        if opcion == '1':
            lista_deseos_cliente = t.ListaDeDeseos(t.productos)
            lista_deseos_cliente.mostrar_productos_disponibles()
            lista_deseos_cliente.simular_agregar_a_lista()
            lista_deseos_cliente.mostrar_lista()


            lista_deseos_cliente.mostrar_productos_disponibles()

            metodo_pago = t.MetodoDePago(t.paises_iva)
            pais_cliente = registro.datos_cliente.get("Pais", "España")
            metodo_pago.procesar_pago(lista_deseos_cliente.lista_deseos, pais_cliente)
            seguimiento = t.SeguimientoPaquetes()
            seguimiento.solicitar_seguimiento()

            # Restaura la lista de productos a la original después de simular agregar a la lista
            lista_deseos_cliente.restaurar_productos_originales()
            break

        elif opcion == '2':
            continue
        elif opcion == '3':
            break

'''
{Fore.RED}
{Fore.GREEN}
{Fore.BLUE}
{Fore.CYAN}
{Fore.MAGENTA}

{Style.RESET_ALL}
'''

