import tienda as t

def preguntar_opcion():
    while True:
        opcion = input("\n¿Qué deseas hacer? (Continuar/Volver/Salir): ").lower()
        if opcion in ['continuar', 'volver', 'salir']:
            return opcion
        else:
            print("Opción no válida. Por favor, elige entre 'Continuar', 'Volver' o 'Salir'.")
if __name__ == '__main__':
    print('¡Bienvenido a la Tienda!')
    t.bienvenida()
    registro = t.RegistroCliente()
    registro.obtener_datos_cliente()
    registro.mostrar_datos_cliente()
    while True:
        opcion = preguntar_opcion()
        if opcion == 'continuar':
            lista_deseos_cliente = t.ListaDeDeseos(t.productos)
            lista_deseos_cliente.mostrar_productos_disponibles()
            lista_deseos_cliente.simular_agregar_a_lista()
            lista_deseos_cliente.mostrar_lista()
            metodo_pago = t.MetodoDePago(t.paises_iva)
            pais_cliente = registro.datos_cliente.get("Pais", "España")
            metodo_pago.procesar_pago(lista_deseos_cliente.lista_deseos, pais_cliente)
            seguimiento = t.SeguimientoPaquetes()
            seguimiento.solicitar_seguimiento()
        elif opcion == 'volver':
            continue
        elif opcion == 'salir':
            break




