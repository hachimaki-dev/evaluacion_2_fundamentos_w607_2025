numeros_ingresados = []


while True:
    print("====Menu Principal====")
    print("1. ingresar un numero")
    print("2. mostrar el numero mayor")
    print("3. Mostrar promedio ")
    print("4. Salir")
    print("======================")


    try:
        opciones = int(input("Ingrese su opcion: "))
    except:
        print("debe ingresar un numero entero")
        continue


  
    if opciones == 1:
        while True:
            try:
                numero = int(input("\nIngrese un número: "))
                if 1 <= numero <= 100:
                    numeros_ingresados.append(numero)
                    print("Ingreso exitoso")
                    break
                else:
                    print("El número debe estar entre 1 y 100")
            except:
                print("Debe ser un número entero")
 
    elif opciones == 2:
        if len(numeros_ingresados) == 0:
            print("no hay numeros en la lista")
        else:
            numero_mayor = max(numeros_ingresados)
            print(f"el numero mayor es: {numero_mayor}")


    elif opciones == 3:
        if len(numeros_ingresados) == 0:
            print("no hay numeros en la lista")
        else:
            promedio = sum(numeros_ingresados) / len(numeros_ingresados)
            print(f"El promedio de los números ingresados es: {promedio:.2f}")


    elif opciones == 4:
        print("\n¡Fin del programa! ¡Adiós!")
        break
    else:
        print("Opción no válida. Por favor, elija una opción del 1 al 4.")

