import random 
numero_1 = 0
numero_2 = 0
numero_aleatorio = 0
resta1 = 0
resta2 = 0
intento1 = 0
intento2 = 0
vidas = 3

print("Bienvenido al juego de adivinanza tu me daras 2 numero\nyo tomare un numero dentro de tal rango y tu tienes que adivinarlo\ntendras 3 intentos, a lo largo del juego te dare pistas, buena suerte")
numero_1 = int(input("ingresar tu primer numero: "))
numero_2 = int(input("Este numero tiene que ser mayor que el primer numero elegido\nfavor ingresar tu segundo numero: "))

numero_aleatorio = random.randint(numero_1, numero_2) 
print("Adivina el numero")

if vidas == 3 :
    intento1 = int(input("Tu primera respuesta es: "))
    if intento1 > numero_aleatorio:
        print("Tu numero es mayor que el mio")
        vidas -= 1 
    elif intento1 < numero_aleatorio:
        print("Tu numero es menor que el mio")
        vidas -= 1
    elif intento1 == numero_aleatorio:
        print("Lo has adivinado, felicidades")
        
    else:
        print("Tu numero ingresado es incorrecto")
        vidas -= 1
else:
    print("ha ocurrido un error")

if vidas == 2: 
    intento2 = int(input("tu segunda respuesta es: "))
    if intento2 > numero_aleatorio:
        print("Tu numero es mayor que el mio")
        resta2 = intento2 - numero_aleatorio
        vidas -= 1
        if intento1 > numero_aleatorio:
            resta1 = intento1 - numero_aleatorio
        elif intento1 < numero_aleatorio:
            resta1 = numero_aleatorio - intento1
        else:
            resta1 = 0
        if resta1 > resta2:
            print("Tu segundo intento estuvo mas cerca")
        elif resta1 < resta2:
            print("Tu primer intento estuvo mas cerca ")
        else:
            print("Ambos intentos estuvieron igual de cerca") 
    elif intento2 < numero_aleatorio:
        print("Tu numero es menor que el mio")
        resta2 = numero_aleatorio - intento2
        vidas -= 1
        if intento1 > numero_aleatorio:
            resta1 = intento1 - numero_aleatorio
        elif intento1 < numero_aleatorio:
            resta1 = numero_aleatorio - intento1
        else:
            resta1 = 0
        if resta1 > resta2:
            print("Tu segundo intento estuvo mas cerca")
        elif resta1 < resta2:
            print("Tu primer intento estuvo mas cerca ")
        else:
            print("Ambos intentos estuvieron igual de cerca")
    elif intento2 == numero_aleatorio:
        print("Has adivinado el numero, felicidades")
if vidas == 1:
    intento3 = int(input("Tu tercer respuesta es: "))
    if intento3 > numero_aleatorio:
        print("Tu numero es mayor que el mio")
        vidas -= 1
    elif intento3 < numero_aleatorio:
        print("Tu numero es menor que el mio")
        vidas -= 1
    elif intento3 == numero_aleatorio:
        print("Adivinaste que pro, felicidades")
    else:
        print("Tu numero ingresado es incorrecto")
        vidas -= 1
if vidas == 0:
    print("Perdiste, es una pena, el numero era: ", numero_aleatorio)