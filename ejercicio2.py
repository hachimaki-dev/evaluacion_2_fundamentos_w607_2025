print("Bienvenido al juego de la adivinanza") 
numero = int(input("Ingrese numero que sea menor al segundo numero"))
numero2 = int(input("Ingrese numero que sea mayor al primero"))    

import random
numero_secreto = random.randint(numero,numero2)



intento1 = int(input("Primer intento"))
if intento1 != numero_secreto:


    if intento1 == numero_secreto:
        print("Felicitaciones,Adivinaste")
    else:
        if intento1 < numero_secreto:
            print("El numero es mayor")
        else:
            print("El numero es menor")

    #Intento 2

    intento2 = int(input("Segundo Intento"))

    if intento2 != numero_secreto:
        
        if intento2 == numero_secreto:
            print("Felecitaciones,Adivinaste")
        else:
            if intento2 < numero_secreto:
                print("El numero es Mayor")
            else:
                print("El numero es Menor")

        distancia = abs(numero_secreto - intento1)
        distancia2 = abs(numero_secreto-intento2)

        if distancia < distancia2:
            print("el primer numero esta mas cerca:", intento1)
        elif distancia2 < distancia:
            print("el segundo numero esta mas cerca", intento2)
        else:
            print("Ambos estan cercas")

        intento3 = int(input("Tercer Intento"))
        if intento3 != numero_secreto:
            if intento3 == numero_secreto:
                print("Adivinaste en el ultimo intento")
            else:
                print("Perdiste el numero es :",numero_secreto)
        else:
            print("Adivinaste Felecidades")

    
    else:
        print("Adivinaste Felecidades")


else:
    print("Adivinaste Felecidades")

