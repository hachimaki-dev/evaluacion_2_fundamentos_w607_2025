import random

def juego_adivinanza():
    print("--Bienvenido al juego de adivinanza--")
    print("Deberas ingresar 2 numeros que representen los limites del numero aleatorio ")
    while True:
        try:
            limite_inferior = int(input("Ingresa el limite inferior: "))
            limite_superior = int(input("Ingresa el limite superior: "))
            if limite_inferior < limite_superior:
                break
            else:
                print("El limite INFERIOR debe ser MENOR al superior, -Intenta nuevamente-")
        except ValueError:
            print("Por favor ingresa un numero entero")

    # numero aleatorio
    numero_aleatorio = random.randint(limite_inferior, limite_superior)
    print("Se ha generado un numero entre:", limite_inferior,"y",limite_superior)

    # intentos
    primer_intento = None
    segundo_intento = None
    for intento in range(1, 4):
        try:
            respuesta = int(input(f"- Intento N°{intento} - Ingresa tu número: "))

            if respuesta == numero_aleatorio:
                print("---¡Felicidades, acertaste el número!---")
                break
            elif respuesta < numero_aleatorio:
                print("El número aleatorio es MAYOR")
            else:
                print("El número aleatorio es MENOR")

            if intento == 1:
                primer_intento = respuesta

            elif intento == 2:
                segundo_intento = respuesta

                if primer_intento is not None and segundo_intento is not None:
                    distancia_1 = abs(numero_aleatorio - primer_intento)
                    distancia_2 = abs(numero_aleatorio - segundo_intento)
                    if distancia_2 < distancia_1:
                        print("Tu segundo intento estuvo más cerca del número aleatorio.")
                    elif distancia_2 > distancia_1:
                        print("Tu primer intento estuvo más cerca del número aleatorio.")
                    else:
                        print("Ambos intentos estuvieron igual de cerca del número aleatorio.")
            elif intento == 3:
                print("-Fallaste- No pudiste adivinar el número aleatorio")
                print("El número aleatorio era:", numero_aleatorio)
        except ValueError:
            print("Ingresa un dato válido")
        
juego_adivinanza()