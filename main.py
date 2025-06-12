def menu():

    print("MENU PRINCIPAL")
    print("1.- Verificar Numero")
    print("2.- Quitar")

while True:
    menu()

    opc = int(input("Ingrese una opcion"))

    if opc == 1:
        print("Ingrese numero")
        while True:
            try:
                numero_entero =int(input())
                if numero_entero > 5:
                    print("el numero es mayor a cinco")
                    break
                elif numero_entero <= 5:
                    print("el numero es igual o menor a cinco")
                    break
            except ValueError:
                print("Intentelo nuevamente")
    elif opc == 2:
        print("Gracias por usar la aplicacion.")
        break
    else:
        print("Opcion Invalida")

