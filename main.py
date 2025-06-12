print("Ingrese un numero entero")

while True:
    try:
        numero_entero =int(input())
        break
    except ValueError:
        print("Intenelo nuevamente")


if numero_entero > 5:
    print("Es mayor que 5.")
else:
    print("Es menor que 5.")