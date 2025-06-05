numeros = []

def ingresar_numeros(numeros):
    while True:
        try:
            num = int(input("Ingrese número: "))
            if 0 <= num <= 100:
                print("Ingreso exitoso.")
                numeros.append(num) # Agrega los números
                break
            else:
                print("Debe ingresar un número entre 0 y 100!!")
        except:
            print("Debe ingresar un número entero!!")


def mayor(numeros):
    if len(numeros) == 0:
        print("No se han ingresado números.")
    else:
        print(f"El número mayor hasta el momento es: {max(numeros)}") # Función de Python que muestra el num mayor


def promedio(numeros):
    suma = 0
    cantidad = len(numeros)
    
    if cantidad == 0:
        print("No se han ingresado números.")
    else:
        for i in range(cantidad):
            suma += numeros[i]
            print(suma)

        promedio = suma/cantidad

        print(f"El promedio de los números ingresados es: {promedio:.2f}")


while True:
    try:
        print("** Menú Principal **")
        print("1. Ingresar números")
        print("2. Mostrar mayor")
        print("3. Mostrar promedio")
        print("4. Salir")
        n = int(input())

        if 0 < n < 5:
            if n == 1:
                ingresar_numeros(numeros)

            elif n == 2:
                mayor(numeros)

            elif n == 3:
                promedio(numeros)

            elif n == 4:
                print("Fin del programa. Adiós.")
                break
        else:
            print("Debe ingresar una opción entre 1 y 4.") # Por si ingresa una opción fuera de rango
    except:
        print("Debe ingresar una opción válida.")