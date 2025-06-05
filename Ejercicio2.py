import time

def menu():
    print("===MENU===")
    print("1. Ingresar Numero")
    print("2. Mostrar Mayor")
    print("3. Mostrar Promedio")
    print("4. Salir")
    opcion_menu = int(input("Ingrese numero : \n"))
    return opcion_menu

numero = None
cant_numeros = 0
numeros = []
def ingresar_numero():
    print("===NUMEROS A INGRESAR===")
    cant_numeros = int(input("¿Cuantos numeros desea ingresar? : \n"))
    while 0 < cant_numeros:
        try:
            print("===INGRESAR NUMERO===")
            numero = int(input("Ingrese el numero : \n"))
            if 0 <= numero <= 100:
                print("Numero Valido.")
                cant_numeros -= 1
                numeros.append(numero) 
                break
            else:
                print("Ingrese un numero dentro del rango (0-100)")
        except ValueError:
            print("Ingrese un numero entero.")

def mostrar_mayor():
    print("===MOSTRAR MAYOR===")
    if numero:
        print(f"El numero mayor es {numero}")

def opciones():
    while True:
        try:
            respuesta_menu = menu()
            if respuesta_menu == 1:
                ingresar_numero()
            elif respuesta_menu == 2:
                mostrar_mayor()
            elif respuesta_menu == 4:
                print("Saliendo del programa...")
                time.sleep(2)
                break
            else:
                print("Ingrese un numero (1-4)")
        except ValueError:
            print("Ingrese un numero valido.")

opciones()