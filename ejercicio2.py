numeros = []

suma = 0

while True:
    print(" ")
    print("---- MENU PRINCIPAL ----")
    print("1.- Ingresar número.    ")
    print("2.- Mostrar mayor.      ")
    print("3.- Mostrar promedio.   ")
    print("4.- Salir.              ")
    print("                        ")

    elegir_opcion = input("Seleccione una opción: ")

    if elegir_opcion == '1':
        while True:
            print(" ")
            ingrese_opcion = input("[-- Ingrese número --] : ")
            print(" ")
            try:
                ingresar_numero = int(ingrese_opcion)
                if 0 <= ingresar_numero <= 100:
                    numeros.append(ingresar_numero)
                    print(" ")
                    print(f"[-- El número {ingresar_numero} ha sido ingresado correctamente --]")
                    print(" ")
                    break
                else:
                    print(" --------------------------------------------- ")
                    print("---- Debe ingresar un número entre 0 y 100 ----")
                    print(" --------------------------------------------- ")
            except ValueError:
                print(" -------------------------------------------------------------------------")
                print("-- Solamente ingresar números enteros (Letras o decimales no permitidos) --")
                print(" -------------------------------------------------------------------------")

    elif elegir_opcion == '2':
        if numeros:
            num_mayor = numeros[0]
            for n in numeros:
                if n > num_mayor:
                    num_mayor = n
            print(" ")
            print(f"[-- El número mayor hasta el momento es: {num_mayor} --]")
        else:
            print(" ")
            print("--- [No se han ingresado números] ---")
            print(" ")

    elif elegir_opcion == '3':
        if numeros:
            for n in numeros:
                suma = (suma + n)
            promedio = suma / len(numeros)
            print(f"-- El promedio de los números ingresados es: {promedio:.2f} --")
        else:
            print(" ")
            print("--- No se han ingresado números. ---")
            print(" ")

    elif elegir_opcion == '4':
        print("Fin del programa.")
        break

    else:
        print(" ----------------------------------------------------------------------------------------------------- ")
        print("opción Inválida, intentelo denuevo [Solo numeros enteros del 1 al 4 (Letras y decimales no permitidos)]")
        print(" ----------------------------------------------------------------------------------------------------- ")