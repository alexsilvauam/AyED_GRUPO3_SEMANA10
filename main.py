cola_tramites = []
historial = {}
historial_tramites = {}

def registrar_tramite(ciudadano, tramite):
    if ciudadano not in historial_tramites:
        historial_tramites[ciudadano] = [] 
    historial_tramites[ciudadano].append(tramite)
    print(f"Trámite '{tramite}' registrado para {ciudadano}.")


def ver_historial(ciudadano):
    if ciudadano in historial_tramites and historial_tramites[ciudadano]:
        print(f"Historial de trámites para {ciudadano}:")
        for tramite in reversed(historial_tramites[ciudadano]):
            print(f" - {tramite}")
    else:
        print(f"No hay historial de trámites para {ciudadano}.")

def mostrar_menu():
    print("\n Menú Principal ")
    print("1. Llegada de ciudadano")
    print("2. Funcionario (requiere acceso)")
    print("3. Salir")

def mostrar_menu_funcionario():
    print("1. Llegada de ciudadano")
    print("2. Atender siguiente ciudadano")
    print("3. Ver cola de espera")
    print("4. Ver historial de un ciudadano")
    print("5. Salir")

# Bucle principal
while True:
    mostrar_menu()
    opcion = input("Elige una opción (1-3): ")

    if opcion == "1":
        nombre = input("Nombre del ciudadano: ")
        tramite = input("Trámite a realizar: ")
        cola_tramites.append((nombre, tramite))
        print(f"{nombre} ha sido agregado a la cola para '{tramite}'.")

    elif opcion == "2":
        clave = input("Ingresa la clave de acceso del funcionario: ")
        if clave == "admin":  
            while True:
                mostrar_menu_funcionario()
                subopcion = input("Elige una opción del menú de funcionario (1-4): ")

                if subopcion == "1":
                    if cola_tramites:
                        print("\nCiudadanos en la cola:")
                        for i, (nombre, tramite) in enumerate(cola_tramites, 1):
                            print(f"{i}. {nombre} - {tramite}")
                    else:
                        print("La cola está vacía.")

                elif subopcion == "2":
                    if cola_tramites:
                        ciudadano, tramite = cola_tramites.pop(0)
                        print(f"Atendiendo a {ciudadano} para '{tramite}'.")
                        if ciudadano not in historial:
                            historial[ciudadano] = []
                        historial[ciudadano].append(tramite)
                    else:
                        print("No hay ciudadanos en la cola.")

                elif subopcion == "3":
                    nombre = input("Nombre del ciudadano para ver historial: ")
                    if nombre in historial and historial[nombre]:
                        print(f"\nHistorial de trámites de {nombre}:")
                        for i, tramite in enumerate(reversed(historial[nombre]), 1):
                            print(f"{i}. {tramite}")
                    else:
                        print(f"{nombre} no tiene trámites registrados.")

                elif subopcion == "4":
                    break
                else:
                    print("Opción no válida. Intenta de nuevo.")
        else:
            print("Clave incorrecta. Acceso denegado.")

    elif opcion == "3":
        print("Saliendo del sistema de trámites.")
        break

    else:
        print("Opción no válida. Intenta de nuevo.")