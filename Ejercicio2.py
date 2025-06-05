#MENU PRINCIPAL
#1.-Ingresar Numero.
#2.-Mostrar numero mayor.
#3.-Mostrar promedio.
#4.-Salir.

numero_mayor = None
acumulador_promedio = 0
contador_promedio =  0

def mostra_menu():

    print("+++++ MENU PRINCIPAL +++++")
    print("1.- Ingresar Numero.")
    print("2.- Mostrar numero Mayor.")
    print("3.- Mostrar promedio.")
    print("4.- Salir.")

def numero_no_ingresado(numero_mayor):

    return numero_mayor is None

while True:
    mostra_menu()
    opcion = input("Seleccione una opcion (1-4): ")
    if opcion == "1":
        try:
            numero = int(input("Ingrese un numero positivo entre 0 y 100!!:"))
            print(f"Se ha registrado exitosamente el numero: {numero}")
            acumulador_promedio = acumulador_promedio + numero
            contador_promedio = contador_promedio + 1
            if numero_mayor is None:
                numero_mayor = numero
            else:
                if numero > numero_mayor:
                    numero_mayor = numero
        except ValueError:
            print("Error: NO ingrese una letra o un numero decimal, debes ingresar un numero entero positivo entre 0 y 100!!.")
        input("Presione Enter para continuar...")

    elif opcion == "2":
        if numero_no_ingresado(numero_mayor):
            print("No se ha ingresado ningun numero.")
        else:
            print(f"El numero mayor es: {numero_mayor}")
        input("Presione Enter para continuar...")
    elif opcion == "3":
        if contador_promedio == 0:
            print("No se ha ingresado un numero para calcular el promedio.")
        else:
            promedio = acumulador_promedio / contador_promedio
            print(f"El promedio de los numeros ingresados es: {promedio}")
        input("Presione Enter para continuar...")
    elif opcion == "4":
        print("Saliendo del programa...")
        break
    else:
        print("Opcion no valida. Tienes que ingresar un numero entre 1 y 4.")
    







