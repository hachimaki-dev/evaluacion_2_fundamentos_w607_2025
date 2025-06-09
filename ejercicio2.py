num_entero = False
numeritos = []

while num_entero == False:
    print("*** MENU PRINCIPAL ***")
    print("1.- Ingresar número.")
    print("2.- Mostrar mayor.")
    print("3.- Mostrar promedio.")
    print("4.- Salir.")
    opcion = int(input())
    if opcion < 1 or opcion > 4:
        print("*** debe ingresar una opcion valida ***")


    try:
        if opcion == 1:
            numero = int(input("Ingrese un numero entre 0 y 100: "))
            if 0 <= numero >= 100:
                print("*** Debe ingresar solo numeros dentro del rango ***")
            else:
                numeritos.append(numero)
                print("el numero se ingreso exitosamente")
    except ValueError:
        print("*** Ingrese solo numeros enteros ***")

    

    if opcion == 2:

        if len(numeritos) == 0:
            print("No se han ingresado numeros")
        else:
            num_mayor = max(numeritos)
            print(f"el numero mayor hasta el momento es: {num_mayor}")

    if opcion == 3:
        promedio = sum(numeritos) / len(numeritos)
        print(f"el promedio de los numeros es: {round(promedio,2)} ")
        
       

    if opcion == 4:
        print("Fin del programa, Adios.")
        num_entero = True
        break
