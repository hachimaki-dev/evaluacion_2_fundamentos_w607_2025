import random

def juego_mental():

    # VARIABLES
    vidas = 3
    num1 = 0
    num2 = 0
    intento1 = 0
    intento2 = 0
    intento3 = 0
    diferencia1 = 0
    diferencia2 = 0
    num_adivinar = 0

    # BIENVENIDA AL JUEGO
    print("===== BIENVENIDO AL JUEGO MENTAL DE ADIVINANZA NUMERICA =====")
    print("Las reglas son simples, tienes que escoger dos números, del 1 al 20 como máximo. Yo escogere un número entre ese rango y tu tratas de adivinarlo")
    print("Tendras 3 intentos para adivinar cuál número escogí, para hacertelo más fácil, te daré pistas")
    print("Te deseo suerte...")

    # INGRESAR NUMEROS POR PARTE DEL USUARIO
    num1 = int(input("Escoge tu primer número: "))
    num2 = int(input("Escoge tu segundo número, tiene que ser mayor al primer número: "))

    # ESCOGER EL RANGO PRESELECCIONADO, DEL 1 AL 20 COMO DICEN LOS REQUISITOS
    if num2 <= num1 or num1 < 1 or num2 > 20:
        print("Rango inválido. Tiene que ser del 1 al 20. Intenta de nuevo")
    else:
        num_adivinar = random.randint(num1, num2) # GENERA EL NÚMERO PARA ADIVINAR
        print("Te menciono que tienes 3 vidas/intentos...")

    # PRIMER INTENTO
    if vidas == 3:
        intento1 = int(input("Tu primer número escogido es: "))
        if intento1 > num_adivinar:
            print("Tu número es mayor que el mio")
            vidas -= 1 # DESCUENTA LA VIDA POR CADA INTENTO FALLIDO, CONSECUENTE CON LOS DEMÁS INTENTOS
        elif intento1 < num_adivinar:
            print("Tu número es menor que el mio")
            vidas -= 1
        elif intento1 == num_adivinar:
            print("¡Correcto! Has adivinado mi número")

    # SEGUNDO INTENTO
    if vidas == 2:
        intento2 = int(input("Tu segundo número escogido es: "))
        if intento2 > num_adivinar:
            print("Tu número es mayor que el mio")
            diferencia2 = intento2 - num_adivinar
            vidas -= 1
        if intento2 < num_adivinar:
            print("Tu número es menor que el mio")
            diferencia2 = num_adivinar - intento2
            vidas -= 1
        elif intento2 == num_adivinar:
             print("¡Correcto! Has adivinado mi número")

    # CALCULAR EL INTENTO QUE ESTUVO MÁS CERCA DEL NÚMERO ELEGIDO POR LA MAQUINA
        if intento1 > num_adivinar:
            diferencia1 = intento1 - num_adivinar
        elif intento1 < num_adivinar:
            diferencia1 = num_adivinar - intento1
        else:
            diferencia1 = 0

    # PISTAS PARA ACERCARSE AL NÚMERO CORRECTO
        if intento2 != num_adivinar:
            if diferencia1 < diferencia2:
                print("Eso estuvo cerca, tu primer número estuvo más cerca al mio...")
            elif diferencia1 > diferencia2:
                print("Tu segundo número estuvo más cerca...")
            else:
                print("Tus dos intentos estuvieron igual de cerca")

    # TERCER INTENTO
        if vidas == 1:
            intento3 = int(input("Tu tercer número escogido es: "))
            if intento3 > num_adivinar:
                print("Tu número es mayor que el mio")
                vidas -= 1
            elif intento3 < num_adivinar:
                print("Tu número es menor que el mio")
                vidas -= 1
            elif intento3 == num_adivinar:
                print("¡Correcto! Has adivinado mi número")

    #FIN DEL JUEGO
        if vidas == 0 and intento1 != num_adivinar and intento2 != num_adivinar and intento3 !=num_adivinar:
            print(f"¡Has perdido! El número que escogí era: {num_adivinar}")

juego_mental()
