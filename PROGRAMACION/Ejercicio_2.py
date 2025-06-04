#MENU PRINCIPAL
# 1.- Ingresar numero.
# 2.- Mostrar numero mayor.
# 3.- Mostrar numero menor.
# 4.- Salir.

numero_mayor = None
numero_menor = None
def mostrar_menu():
    
    print("***MENU PRINCIPAL***")
    print("1.- Ingresar numero.")
    print("2.- Mostrar numero mayor.")
    print("3.- Mostrar numero menor.")
    print("4.- Salir.")

def no_numeros_ingresados(numero_mayor, numero_menor):
    
    return numero_mayor is None and numero_menor is None

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción (1-4): ")
    if opcion == "1":
        try:
            numero = int(input("Ingrese un numero positivo entre 0 y 100: "))
            print(f"Se ha ingresado elnumero con exito.")
            if numero_mayor is None and numero_menor is None:
                numero_mayor = numero
                numero_menor = numero
            else:
                if numero > numero_mayor:
                    numero_mayor = numero
                if numero < numero_menor:
                    numero_menor = numero
        # Se lanza esta excepción si el usuario ingresa un valor que no es un número entero.
        except ValueError:
            print("Por favor, debes ingresar un número entero.")
        input("Presione Enter para continuar...")
    elif opcion == "2":
        if no_numeros_ingresados(numero_mayor, numero_menor):
            print("No se ha ingresado ningun numero.")
        else:
            print(f"El numero mayor es: {numero_mayor}")
        input("Presione Enter para continuar...")
    elif opcion == "3":
        if no_numeros_ingresados(numero_mayor, numero_menor):
            print("No se ha ingresado ningun numero.")
        else:
            print(f"El numero menor es: {numero_menor}")
        input("Presione Enter para continuar...")    
    elif opcion == "4":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida, por favor ingrese un número entre 1 y 4.")

#Fin del ejercicio.





