def menu():
    print("\nGestión de clientes:")
    print("(1) Añadir cliente")
    print("(2) Eliminar cliente")
    print("(3) Mostrar cliente")
    print("(4) Listar todos los clientes")
    print("(5) Listar clientes preferentes")
    print("(6) Terminar")
    return input("Elige una opción: ")

def agregar_cliente(clientes):
    nif = input("NIF: ")
    nombre = input("Nombre: ")
    direccion = input("Dirección: ")
    telefono = input("Teléfono: ")
    correo = input("Correo electrónico: ")
    preferente = input("¿Es preferente? (s/n): ").lower() == 's'
    clientes[nif] = {
        'nombre': nombre,
        'direccion': direccion,
        'telefono': telefono,
        'correo': correo,
        'preferente': preferente
    }

def eliminar_cliente(clientes):
    nif = input("Introduce el NIF del cliente a eliminar: ")
    if nif in clientes:
        del clientes[nif]
        print("Cliente eliminado.")
    else:
        print("Cliente no encontrado.")

def mostrar_cliente(clientes):
    nif = input("Introduce el NIF del cliente: ")
    cliente = clientes.get(nif)
    if cliente:
        print(f"Datos de {nif}: {cliente}")
    else:
        print("Cliente no encontrado.")

def listar_clientes(clientes):
    for nif, datos in clientes.items():
        print(f"NIF: {nif} - Nombre: {datos['nombre']}")

def listar_preferentes(clientes):
    for nif, datos in clientes.items():
        if datos['preferente']:
            print(f"NIF: {nif} - Nombre: {datos['nombre']}")

if __name__ == "__main__":
    clientes = {}
    while True:
        opcion = menu()
        if opcion == '1':
            agregar_cliente(clientes)
        elif opcion == '2':
            eliminar_cliente(clientes)
        elif opcion == '3':
            mostrar_cliente(clientes)
        elif opcion == '4':
            listar_clientes(clientes)
        elif opcion == '5':
            listar_preferentes(clientes)
        elif opcion == '6':
            print("Programa terminado.")
            break
        else:
            print("Opción no válida.")