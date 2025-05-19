from random import randint

while True:
    numero_menor = int(input("seleccione el numero menor\n"))
    numero_mayor = int(input("seleccione el numero mayor\n"))
    if numero_menor<numero_mayor:
        break
    else:
        print("el primer numero debe ser menor que el segundo")

numero_adivinar = randint(numero_menor, numero_mayor)

intento1 = int(input("intenta adivinar el numero\n"))

if intento1 != numero_adivinar:
    if numero_adivinar < intento1:
        print("el numero es menor")
    else: print("el numero es mayor")
    intento2 = int(input("intentalo de nuevo\n"))
    
    if intento2 != numero_adivinar:
        
        if numero_adivinar < intento2:
            print("el numero es menor")
        else: 
            print("el numero es mayor")

        distancia1 = abs(numero_adivinar - intento1)
        distancia2 = abs(numero_adivinar - intento2)
        print("te dare una pista")

        if distancia1 < distancia2:
            print(f"el numero que buscas esta mas cerca de {intento1} que de {intento2}")
        elif distancia1 > distancia2:
            print(f"el numero que buscas esta mas cerca de {intento2} que de {intento1}")
        else:
            print(f"el numero esta a la misma distancia de {intento1} y {intento2}")
        intento3 = int(input("intente por ultima vez\n"))
        
        if intento3 != numero_adivinar:
            print("perdiste, el numero era " , numero_adivinar)
        else:
            print("felicidades, adivinaste en el ultimo intento")
    else: 
        print("felicidades, adivinaste el numero en el segundo intento")
else: 
    print("felicidades, adivinaste el numero en el primer intento")