print("Ingrese un numero entero")
numero_entero = 0

while True:
    try:
        numero_entero =int(input())
        break
    except ValueError:
        print("Intenelo nuevamente")
if numero_entero >= 5:
    print("Es mayor a 5")
else:
     print("es memor a 5")