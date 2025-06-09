numeros = []
menu = 1
while menu == True:   
    print("##### MENÚ #####")
    print("1.- Ingresar número.")
    print("2.- Mostrar mayor.")
    print("3.- Mostrar promedio.")
    print("4.- Salir.")

    opcion = int(input("Selecciona 1-4: "))

    while True:
        try:
            if opcion == 1:
                numero = int(input("Inngrese un número: "))
                if numero < 0 or numero > 100:
                    print("Debe ingresar un numero entre 0 y 100!!")
                else:
                    print("Ingreso exitoso.")
                    numeros.append(numero)
                break
        except ValueError:
            print("Debe ingresar un número entero!!")
        if opcion == 2:
            if numeros:
                print("El número mayor hasta el momento es: ", max(numeros))
                break
                
            else:
                print("No se han ingresado números.")

    
        if opcion == 3:
            suma = sum(numeros)
            cantidad = len(numeros)
            promedio = suma/cantidad
            print(numeros)
            print(f"El promedio de los numeros ingresados es: {promedio}")
            break

        if opcion == 4:
            menu == False
        if opcion > 4:
            print("Debe ingresar una opcion válida.")