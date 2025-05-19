from random import randint
print("Juego de adivinanza")
limite_inferior =int(input("Ingresa el número inferior del rango: "))
limite_superior =int(input("Ingresa el número superior del rango: "))

numero_secreto = randint(limite_inferior, limite_superior)
for intento in range(1,20):
    respuesta = int(input(f"Intento {intento} - Adivina el número: "))
    
    if respuesta == numero_secreto:
        print(f"¡Felicitaciones! Adivinaste el número en el intento {intento}.")
        break
    else:
        print("No es el número. Intenta de nuevo.")

else:
    print(f"Lo siento, no adivinaste. El número era {numero_secreto}")

       



