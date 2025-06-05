menu = True
numeros = []
cantidaddenumeros = 0

while menu == True:
    try:
        print("***MENU PRINCIPAL***")
        print("1.- Ingresar número")
        print("2.- Mostrar mayor")
        print("3.- Mostrar promedio")
        print("4.- Salir")
        opcion = int(input())

        if opcion == 1:
            dato = False
            while dato == False:
                try:
                    numero = int(input("Ingrese un número entre 0 y 100\n"))
                    if numero >= 0 and numero <= 100:
                        print("Ingreso exitoso")
                        numeros.append(numero)
                        cantidaddenumeros = cantidaddenumeros + 1
                        dato = True
                    else:
                        print("Debe ingresar un número entre 0 y 100!")
                except ValueError:
                    print("Debe ingresar un número entero")

        elif opcion == 2:
            if numero:
                print(f"El número mayor hasta el momento es: {max(numeros)}")
            else:
                print("No se han ingresado números")

        elif opcion == 3:
            if numero:
                suma = sum(numeros)
                promedio = suma / cantidaddenumeros
                print(f"El promedio de los números ingresados es: {promedio:.1f}")
            else:
                print("No se han ingresado números")

        elif opcion == 4:
            print("Fin del programa. Adiós")
            menu = False

        else:
            print("Debe ingresar una opción válida")

    except ValueError:
        print("Debe ingresar una opción válida")