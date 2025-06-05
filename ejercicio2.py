opcion = 0
numeros_ingresados = []
while opcion != 4:
    try:
        print("1. Ingresar numero")
        print("2. Mostrar mayor")
        print("3. Mostrar promedio")
        print("4. Salir ")
        opcion = int(input("Porfavor ingrese una opcion: "))

        while opcion < 1 or opcion > 4:
            try:
                opcion = int(input("Porfavor ingrese una numero entero valido: "))
            except ValueError:
                print("Error 202: Solo puede ingresar numeros")

        if opcion == 1:
            num = 0
            while num < 1 or num > 100:
                try:
                    num = int(input("Porfavor ingrese un numero valido entre 1 y 100: "))
                except ValueError:
                    print("Error 202: Solo puede ingresar numeros")

            numeros_ingresados.append(num)
            print("Ingreso exitoso, tus numeros son: ",numeros_ingresados)
            

        if opcion == 2:
            if numeros_ingresados:
                max_v = max(numeros_ingresados)
                print("El numero mayor ingresado hasta ahora es: ",max_v )
            else:
                print("No se han ingresado numeros. Porfavor ingresa datos")
                
        if opcion == 3:
            if numeros_ingresados: 
                prom = sum(numeros_ingresados) / len(numeros_ingresados)
                print(f"El promedio es {prom:.2f}")
            else:
                print("no se han ingresado numeros")

        if opcion == 4:
            print("Gracias por usar el programa. creador: Sebastian Mansilla")

    except ValueError:
        print("Error 202: Solo puede ingresar numeros")