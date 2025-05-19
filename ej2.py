from random import randint

limite_inferior = int(input("Ingrese límite inferior: "))
limite_superior = int(input("Ingrese límite superior: "))

numero_secreto = randint(limite_inferior, limite_superior)

intentos = [ ]

adivina = int(input("Intente adivinar: "))
intentos.append(adivina)

if adivina == numero_secreto:
    print("¡Felicitaciones, adivinaste!")
else:
    if adivina < numero_secreto:
        print("El número es mayor.")
    else:
        print("El número es menor.")

    adivina = int(input("Intente de nuevo: "))
    intentos.append(adivina)

    if adivina == numero_secreto:
        print("¡Felicitaciones, adivinaste!")
    else:
        if adivina < numero_secreto:
            print("El número es mayor.")
        else:
            print("El número es menor.")

        if numero_secreto > intentos[0]:
            dif1 = numero_secreto - intentos[0]
        else:
            dif1 = intentos[0] - numero_secreto

        if numero_secreto > intentos[1]:
            dif2 = numero_secreto - intentos[1]
        else:
            dif2 = intentos[1] - numero_secreto

        if dif2 < dif1:
            print("El número que buscas está más cerca de", intentos[1], "que de", intentos[0])
        else:
            print("El número que buscas está más cerca de", intentos[0], "que de", intentos[1])

        adivina = int(input("Intente la última vez: "))
        if adivina == numero_secreto:
            print("¡Felicitaciones, adivinaste!")
        else:
            print("Perdiste.")
            print("El número era:", numero_secreto)
