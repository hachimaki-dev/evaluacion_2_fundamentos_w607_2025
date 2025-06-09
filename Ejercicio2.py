import time

def menu():
    print("===MENU PRINCIPAL===")
    print("1. Ingresar Numero")
    print("2. Mostrar Mayor")
    print("3. Mostrar Promedio")
    print("4. Mostrar Numeros Guardados")
    print("5. Salir")
    try:
        opcion = int(input("Ingrese opcion : \n"))
        return opcion
    except ValueError:
        print("Ingrese un numero valido.")
        return None

numeros = []

while True:
    opcion = menu()

    if opcion == 1:
        while True:
            try:
                num_ingresado = int(input("Ingrese un numero (0 - 100): \n"))
                if 0 <= num_ingresado <= 100:
                    numeros.append(num_ingresado)
                    print(f"Ingreso exitoso, {num_ingresado}")
                    break
                else:
                    print("Debe estar dentro del rango!! (0-100)")
            except ValueError:
                print("Ingrese numero valido.")
    elif opcion == 2:
        if numeros:
            mayor = max(numeros)
            print(f"Numero mayor : {mayor}")
        else:
            print("No hay numeros ingresados.")
    elif opcion == 3:
        if numeros:
            promedio = sum(numeros) / len(numeros)
            print(f"Promedio : {promedio: .2f}")
        else:
            print("No hay numeros ingresados.")
    elif opcion == 4:
        if numeros:
            print(f"Numeros guardados: {numeros}")
        else:
            print("No hay numeros guardados.")
    elif opcion == 5:
        print("Saliendo del programa...")
        time.sleep(2)
        break
    elif opcion is None:
        continue
    else:
        print("Opcion no valida.")