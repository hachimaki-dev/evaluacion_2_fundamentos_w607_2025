print("Ingrese un numero entero")

while True:
    try:
        numero_entero =int(input())
        break
    except ValueError:
        print("Intenelo nuevamente")


if numero_entero > 5:
    print("Tu numero es mayor que 5")
else:
    numero_entero < 5
    print("Tu numero es menor que 5")
    