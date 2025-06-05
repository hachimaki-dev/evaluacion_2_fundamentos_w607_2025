numeros = []

while True:
    print(" ")
    print("---- MENU PRINCIPAL ----")
    print("1.- Ingresar número.")
    print("2.- Mostrar mayor.")
    print("3.- Mostrar promedio.")
    print("4.- Salir.")
    print(" ")

    opciones = input("Seleccione una opción: ")

    if opciones == '1':
        while True:
            ingrese_opcion = input("Ingrese número: ")
            try:
                ingresar_numero = int(ingrese_opcion)
                if 0 <= ingresar_numero <= 100:
                    numeros.append(ingresar_numero)
                    print("--- [Ingreso exitoso] ---")
                    break
                else:
                    print("---- Debe ingresar un número entre 0 y 100 ----")
            except ValueError:
                print("-- Debe ingresar un número entero --")

    elif opciones == '2':
        if numeros:
            num_mayor = numeros[0]
            for n in numeros:
                if n > num_mayor:
                    num_mayor = n
            print(" ")
            print(f"[-- El número mayor hasta el momento es: {num_mayor} --]")
        else:
            print("--- [No se han ingresado números] ---")

    elif opciones == '3':
        if numeros:
            suma = 0
            for n in numeros:
                suma = (suma + n)
            promedio = suma / len(numeros)
            print(f"-- El promedio de los números ingresados es: {promedio} --")
        else:
            print("--- No se han ingresado números. ---")

    elif opciones == '4':
        print("Fin del programa.")
        break

    else:
        print("Debe ingresar una opción válida.")