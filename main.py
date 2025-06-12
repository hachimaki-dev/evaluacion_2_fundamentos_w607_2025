print("Ingrese un numero entero")

while True:
    try:
        numero_entero =int(input())
        break
    except ValueError:
        print("Intenelo nuevamente")
