numeros = []

while True:
    print("*** MENU PRINCIPAL ***")
    print("1. Ingresar número.")
    print("2. Mostrar mayor.")
    print("3. Mostrar promedio.")
    print("4. Salir.")

    opcion = input("Elija opción: ")

    if opcion == "1":
        # Ingresar número
        while True:
            try:
                numero = int(input("Ingrese un número entero entre 0 y 100: "))
                if 0 <= numero <= 100:
                    numeros.append(numero)
                    print("Ingreso exitoso")
                    break
                else:
                    print("Debe ingresar un número entre 0 y 100!!")
            except:
                print("Debe ingresar un número entero!!")

    elif opcion == "2":
        # Mostrar número mayor
        if numeros:
            print("El número mayor hasta el momento es:", max(numeros))
        else:
            print("No se han ingresado números.")

    elif opcion == "3":
        # Mostrar promedio
        if numeros:
            promedio = sum(numeros) / len(numeros)
            print("El promedio de los números ingresados es:", (promedio))
        else:
            print("No se han ingresado números.")

    elif opcion == "4":
        print("Fin del programa. Adiós.")
        break

    else:
        print("Debe ingresar una opción válida.")