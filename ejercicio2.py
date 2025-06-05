menu = True
numeros = []

while menu == True:
    try:
        print("***MENU PRINCIPAL***")
        print("1.- Ingresar número")
        print("2.- Mostrar mayor")
        print("3.- Mostrar menor")
        print("4.- Salir")
        opcion = int(input())

        if opcion == 1:
            try:
                numero = int(input("Ingrese un número entre 0 y 100"))
                if numero >= 0 and numero <= 100:
                    print("Ingreso exitoso")
                else:
                    print("Debe ingresar un número entre 0 y 100!")
            except ValueError:
                print("Debe ingresar un número entero")


    except ValueError:
        print("Debe ingresar una opción válida")