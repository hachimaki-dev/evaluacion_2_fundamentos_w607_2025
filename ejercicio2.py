# Ejercicio 2: Sistema de Menú con Manejo de Números
numeros = []
promedio = 0.0
def menuPrincipal():
    while True:
        try:
            print("Bienvenido a este nuevo menú interactivo en donde tienes la posibilidad de ingresar tantos numeros como desees, saber qué numero es mayor y poder sacar el promedio")
            print("Sigue atentamente las instrucciones a continuación: ")

            print("==========MENÚ PRINCIPAL===========")
            print("1. Ingresar un número")
            print("2. Mostrar número mayor")
            print("3. Mostrar promedio")
            print("4. Salir")

            print("====================================")

            eleccion = input("Elige una opción: ") 

            print("====================================")
            print("Ingreso exitoso")


            if eleccion == "1":
                ingresarNumero()
            elif eleccion == "2":
                mostrarMayor()
            elif eleccion == "3":
                mostrarPromedio()
            else:
                eleccion == "4"
                print("====================================")            
                print("¡¡¡Vuelve pronto!!!")
                break
        except ValueError:
            print("ERROR")



def ingresarNumero():
    while True:
        numeroSTR = int(input("Ingrese un número del 0 al 100: "))
        print("====================================")
        try: 
            if 0 <= numeroSTR <= 100:
                numeros.append(numeroSTR)
                print("Ingreso exitoso")
                print("====================================")
                print("Tu número agregado es:", numeroSTR)
                break
            else:
                print("El número ingresado debe estar entre el 0 y el 100")
        except ValueError:
            print("Por favor, ingrese un número válido")
    input("Para regresar precione la tecla Enter")

def mostrarMayor():
    if len(numeros) == 0:
          print("Aún no se han ingresado números")
    else:
        numeroMayor = max(numeros)
        print("El número mayor hasta ahora es: ", numeroMayor)
        print("====================================")
        input("Para regresar precione la tecla Enter")


def mostrarPromedio():
    while True:
        try:
            if numeros:
                promedio = sum(numeros) / len(numeros)
                print(f"El promedio de los números es: {promedio:.2f}")
        except ValueError:
                print("No se han ingresado números")  



menuPrincipal()

