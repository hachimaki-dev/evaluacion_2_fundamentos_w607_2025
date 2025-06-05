def menu_interactivo():
    numeros = []
    while True:
        try:
            opcion = int(input("*** MENU PRINCIPAL ***\n"
                        "1.- Ingresar número.\n"
                        "2.- Mostrar mayor.\n"
                        "3.- Mostrar promedio.\n"
                        "4.- Salir.\n"
                        "Selecciona una opcion: "))
            # Opciones
            if opcion == 1:
                while True:
                    try:
                        numero_usuario = int(input("Ingresa el numero: "))
                        if 0 <= numero_usuario <= 100:
                            print("Ingreso Exitoso\n")
                            numeros.append(numero_usuario)
                            break
                        else:
                            print("Debe ingresar un numero entre 0 y 100!!\n")
                    except ValueError:
                        print("Debe ingresar un numero entero\n")
            elif opcion == 2:
                if numeros:
                    print("El numero mayor hasta el momento es:",max(numeros))
                else:
                    print("No se han ingresado numeros\n")
            elif opcion == 3:
                if numeros:
                    promedio = sum(numeros)/len(numeros)
                    print(f"El promedio de los numeros ingresados es: {promedio:.2f}")
                else:
                    print("No se han ingresado numeros\n")
            elif opcion == 4:
                print("Fin del programa, Adios.")
                break
            else:
                print("Debe ingresar una opcion valida\n")
        except ValueError:
            print("Debe ingresar una opcion valida\n")
menu_interactivo()