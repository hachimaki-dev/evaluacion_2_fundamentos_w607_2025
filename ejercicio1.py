numeros = []

while True:
    print("\n--MENU PRINCIPAL--")
    print("1-ingresar numero")
    print("2-mostrar mayor")
    print("3-mostrar promedio")
    print("4-salir")

    try:
        opcion = int(input("ingrese su opcion"))
    except ValueError:
        print("debe ingresar un numero entero para la opcion.")
        continue

    if opcion == 1:
        try:
            numero = int(input("ingrese un numero entero entre 0 y 100"))
        except ValueError:
            print("debe ingresar un numero entero valido")

    elif opcion == 2:
        if numeros:
             print("El número mayor es:", max(numeros))
        else:
            print("Aún no se han ingresado números.")

    elif opcion == 3:
        if numeros:
            promedio = sum(numeros) / len(numeros)
            print("El promedio es:", promedio)
        else:
            print("aun no se han ingresado numeros")

    elif opcion == 4:
        print("Saliendo del programa...")
        break
    
    else:
        print("Opción no válida. Intente nuevamente.")