numeros = []

while True:
    try:
        print("\n*** Menú Principal ***")
        print("1. Ingresar número")
        print("2. Mostrar mayor")
        print("3. Mostrar promedio")
        print("4. Salir")

        opcion = int(input("Ingrese una opcion: "))
        if opcion == 1:
            while True:
                try:
                    num = input("Ingrese un número entre 0 y 100: ")
                    n = int(num)
                    if n < 0 or n > 100:
                        print("Debe ingresar un número entre 0 y 100!!")
                        continue
                    print("Ingreso exitoso.")
                    numeros.append(num)
                    break
                except ValueError:
                    print("Debe ingresar un numero entero!!")
        elif opcion == 2:
            if not numeros:
                print("No se han ingresado numeros")
            else:
                print(f"El numero mayor es: {max(numeros)}")
        elif opcion == 3:
            prom = sum(numeros) / len(numeros)
            print(f"El promedio de los numeros es {prom}")
        elif opcion == 4:
            print("Fin del programa. Adios")
            break
        else:
            print("Debe ingresar una opción valida.")
    except ValueError:
        print("Ingrese una opción valida")