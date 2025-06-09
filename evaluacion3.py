numeros = []

def menu_interactivo():

    print("***MENU PRINCIPAL***")
    print("1.- Ingresar Número")
    print("2.- Mostrar Mayor")
    print("3.- Mostrar Promedio")
    print("4.- Ver Numeros Guardados")
    print("5.- Salir")

while True:
    menu_interactivo()
    opcion = int(input("Ingrese una opcion: "))
        
    if opcion == 1:
        while True:
            try:
                numero = int(input("Ingrese número: "))
                if 0 <= numero <= 100:
                    numeros.append(numero)               
                    break
                else:
                    print("Debe ingresar un número entre 0 y 100!!")
            except ValueError:
                print("Debe ingresar un número entero!!")

    elif opcion == 2:
        if numeros:
            print ("El número mayor hasta el momento es: ", max(numeros))
        else:
            print ("No se han ingresado números.")

    elif opcion == 3:
        if numeros:
                promedio = sum(numeros) / len(numeros)
                print(f"El promedio de los números ingresados es: , {promedio:.2f}")
        else:
            print("No se han ingresado números.")        

    elif opcion == 4:
        if numeros:
            print("Los numeros registrados son: ", numeros)
        else:
            print ("No se han ingresado números.")

    elif opcion == 5:
        print("Fin del programa. Adiós.")
        break

    else:
        print("Debe ingresar una opción válida.")
    

