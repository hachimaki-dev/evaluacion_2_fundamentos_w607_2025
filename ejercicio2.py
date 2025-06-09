
numeros = []

while True:
    print(" ---Menu Principal --")
    print("1.- Ingrese un numero.")
    print("2.- Mostrar mayor.")
    print("3.- Mostrar promedio.")
    print("4.- Salir.")

    try:
        opcion = int(input("Ingrese una opción: "))
    except:
        print("Debe ingresar una opción válida.")
        continue

    if opcion == 1:
        while True:
            try:
                numero = int(input("Ingrese un número: "))
                if 0 <= numero <= 100:
                    numeros.append(numero)
                    print("Ingreso exitoso")
                    break
                else:
                    print("Debe ingresar un número entre 0 y 100")
            except:
                print("Debe ingresar un número entero!!")

    elif opcion == 2:
        if len(numeros) == 0:
            print("No se han ingresado números.")
        else:
            print("El número mayor hasta el momento es:", max(numeros))

    elif opcion == 3:
        if len(numeros) == 0:
            print("No se han ingresado números.")
        else:
            promedio = sum(numeros) / len(numeros)
            print("El promedio de los números ingresados es:" , promedio )

    elif opcion == 4:
        print("Fin del programa.")
        break

    else:
        print("Debe ingresar una opción válida.")
