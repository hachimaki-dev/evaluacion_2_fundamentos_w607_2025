import random
numero1 = 0
numero2 = 0
numero_adivinar = 0
diferencia1 = 0
diferencia2 = 0
intento1 = 0
intento2 = 0
vidas = 3

print("bienvenido al juego de adivinanza tu me daras 2 numero\nyo tomare un numero dentro de ese rango y tu deberas adivinarlo\ntendras 3 intentos, a lo largo del juego te dare diferentes pistas, buena suerte")
while True:
    numero1 = int(input("favor ingresar tu primer numero: "))
    numero2 = int(input("recuerda que el siguiente numero debe ser mayor que el segundo\nfavor ingresar tu segundo numero: "))
    if numero2 > numero1:
        break
numero_adivinar = random.randint(numero1, numero2)
#lo de arriba lo hice para forzar a que el numero 2 sea mayor que el numero 1, si no es asi, simplemente se repite
#podria haber usado un bouliano pero el break cumple la funcion, asi es mas corto y simple

print("trata de adivinar mi numero")
if vidas == 3 :
    intento1 = int(input("tu primera respuesta es: "))
    if intento1 > numero_adivinar:
        print("tu numero es mayor que el mio")
        vidas -= 1 #de esta forma me ahorro tener que escribir: vidas = vidas - 1
    elif intento1 < numero_adivinar:
        print("tu numero es menor que el mio")
        vidas -= 1
    elif intento1 == numero_adivinar:
        print("Felicitaciones adivinaste")
        
    else:
        print("tu numero ingresado es incorrecto")
        vidas -= 1

if vidas == 2:
    intento2 = int(input("tu segunda respuesta es: "))
    if intento2 > numero_adivinar:
        print("tu numero es mayor que el mio")
        diferencia2 = intento2 - numero_adivinar
        diferencia1 = intento1 - numero_adivinar
        diferencia1 = abs(diferencia1) #utilizo abs en caso que el resultado sea negativo lo pasa a positivo porque usar <> en negativos arruina la formula
        if diferencia1 > diferencia2:
            print("tu segundo intento estuvo mas cerca")
        elif diferencia1 < diferencia2:
            print("tu primer intento estuvo mas cerca ")
        else:
            print("ambos intentos estuvieron igual de cerca")
        vidas -= 1
    elif intento2 < numero_adivinar:
        print("tu numero es menor que el mio")
        diferencia2 = numero_adivinar - intento2
        diferencia1 = intento1 - numero_adivinar
        diferencia1 = abs(diferencia1)
        if diferencia1 > diferencia2:
            print("tu segundo intento estuvo mas cerca")
        elif diferencia1 < diferencia2:
            print("tu primer intento estuvo mas cerca ")
        else:
            print("ambos intentos estuvieron igual de cerca")
        vidas -= 1
    elif intento2 == numero_adivinar:
        print("Felicitaciones adivinaste")
    else:
        print("tu numero ingresado es incorrecto")
        vidas -= 1
if vidas == 1:
    intento1 = int(input("tu tercer respuesta es: "))
    if intento1 > numero_adivinar:
        print("tu numero es mayor que el mio")
        vidas -= 1
    elif intento1 < numero_adivinar:
        print("tu numero es menor que el mio")
        vidas -= 1
    elif intento1 == numero_adivinar:
        print("Felicitaciones adivinaste")
    else:
        print("tu numero ingresado es incorrecto")
        vidas -= 1
if vidas == 0:
    print("perdiste, mi numero era: ", numero_adivinar)
