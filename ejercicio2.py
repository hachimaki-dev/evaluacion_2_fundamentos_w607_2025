numeros = []  # Lista para almacenar los números ingresados por el usuario
promedio = 0.0  # Variable inicial para el promedio, 0.0 debido a que el promedio es posible que igual pueda dar decimal

# Bucle infinito del menú
while True:
    print("=== MENU PRINCIPAL ===\n")
    print("1.- Ingresar número")
    print("2.- Mostrar mayor")
    print("3.- Mostrar promedio")
    print("4.- Salir.")

    # Opción para elegir dentro del menú
    try:
        opcion = int(input("Elige una opción: "))
    except ValueError:
        print("Debe ingresar una opción válida.")
        continue # Vuelve a mostrar el menú en caso de opción inválida

    # Opción 1 - Ingresar número entre el 0 y 100
    if opcion == 1:
        while True: # Sigue pidiendo y repitiendo hasta que el número sea válido
            try:
                n = int(input("Ingrese un número entero entre 0 y 100: "))
                if 0 <= n <= 100:
                    numeros.append(n) # El número ingresado por el usuario es mandado a la lista llamada "numeros"
                    print("Ingreso exitoso")
                    break # Sale del bucle y vuelve al menú principal
                else:
                    print("Debe ingresar un número entre 0 y 100!!") # En caso de ingresar un número menor a 0 y mayor a 100
            except ValueError:
                print("Debe ingresar un número entero!!") # En caso de ingresar un número décimal

    # Opción 2 - Mostrar el mayor número
    elif opcion == 2:
        if numeros:
            print(f"El número mayor hasta el momento es: {max(numeros)}") # Dentro de la lista "numeros", busca el número mayor entre todos los ingresados por el usuario
        else:
            print("No se han ingresado números") # En caso de estar la lista vacía

    # Opción 3 - Mostrar el promedio 
    elif opcion == 3:
        if numeros:
            promedio = sum(numeros) / len(numeros) # El promedio se calcula con la suma total de los numeros dentro de la lista y diviendolos por la cantidad de numeros en total que hay en está, para eso se utiliza el len. Ej: (10, 20, 30 = 60 / 3)
            print(f"El promedio de los números ingresados es: {promedio:.2f}")
        else:
            print("No se han ingresado números")

    # Opción 4 - Finalizar programa
    elif opcion == 4:
        print("Finalizando programa...")
        print("Adios")
        break # Cierre del bucle del menú

    # Cualquier opción del menú que sea inválida
    else:
        print("Debe ingresar una opción válida.")
