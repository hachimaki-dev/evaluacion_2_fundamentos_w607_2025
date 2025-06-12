print("Ingrese un numero entero")

while True:
    try:
        numero_entero =int(input())
        break
    except ValueError:
        print("Intenelo nuevamente")
if numero_entero >= 5:
    print("El numero es mayor o igual a 5")
else:
    print("El numero es menor a 5")
