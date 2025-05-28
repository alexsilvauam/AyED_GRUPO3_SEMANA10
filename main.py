
cola_tramites = []
historial = {}

def mostrar_menu():
    print(" Menu ")
    print("1. Llegada de ciudadano")
    print("2. Atender siguiente ciudadano")
    print("3. Ver cola de espera")
    print("4. Ver historial de un ciudadano")
    print("5. Salir")

while True:
    mostrar_menu()
    opcion = input("Elige una opción (1-5): ")
    
    if opcion == "1":
        nombre = input("Nombre del ciudadano: ")
        tramite = input("Trámite a realizar: ")
        cola_tramites.append((nombre, tramite))
        print(f"{nombre} ha sido agregado a la cola para '{tramite}'.")

    elif opcion == "2":
        if cola_tramites:
            ciudadano, tramite = cola_tramites.pop(0)
            print(f"Atendiendo a {ciudadano} para '{tramite}'.")
            if ciudadano not in historial:
                historial[ciudadano] = []
            historial[ciudadano].append(tramite)
        else:
            print("No hay ciudadanos en la cola.")

    elif opcion == "3":
        if cola_tramites:
            print("\nCiudadanos en la cola:")
            for i, (nombre, tramite) in enumerate(cola_tramites, 1):
                print(f"{i}. {nombre} - {tramite}")
        else:
            print("La cola está vacía.")

    elif opcion == "4":
        nombre = input("Nombre del ciudadano para ver historial: ")
        if nombre in historial and historial[nombre]:
            print(f"\nHistorial de trámites de {nombre}:")
            for i, tramite in enumerate(reversed(historial[nombre]), 1):
                print(f"{i}. {tramite}")
        else:
            print(f"{nombre} no tiene trámites registrados.")

    elif opcion == "5":
        print("Saliendo del sistema de trámites.")
        break

    else:
        print("Opción no válida. Intenta de nuevo.")