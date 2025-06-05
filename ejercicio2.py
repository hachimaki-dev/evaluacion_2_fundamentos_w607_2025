numeros =[]

while True:
    print("***MENU PRINCIPAL")
    print("1.ingrese su numero")
    print("2.ingrese el mayor")
    print("3.mostrar promedio")
    print("4.salir")
        

    opcion = input("Seleccione una opcion:")
     
    if opcion == "1":
        while True:
            try:
                entrada = input("Ingrese un numero")
                numero = int(entrada)
                if 0 <= numero <= 100:
                    numeros.append(numero)
                    print("ingreso exitoso")
                    break
                else:
                    return entrada
                    print("Ingrese un numero del 0 al 100")
            except:
                print("Ingrese un numero entero")

    elif opcion == "2":
        if len(numeros) ==0:
            print("no se han ingresado numeros")
        else:
            print("El numero mayor es",max(numeros))

    elif opcion == "3":
        if len(numeros) ==0:
            print("no se han ingresado numeros")
        else:
            promedio = sum(numeros) / len(numeros)
            print("El promedio de los numeros es", promedio)

    elif opcion == "4":
        print("Fin del programa adios")
        break
    else:
        print("Elija una opcion valida")

   
    
        





