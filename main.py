print("Ingrese un numero entero")

while True:
    try:
        numero_entero =int(input())
        if numero_entero > 5:
            print("El numero es mayor a 5")
        break
    except ValueError:
        print("Intenelo nuevamente")
      