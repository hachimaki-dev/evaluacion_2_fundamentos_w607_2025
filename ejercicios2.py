#Generar un numero aleatorio
from random import randint #Con esto importamos una biblioteca de python, para generar
#correctamente un numero aleatorio
print("Juego para adivinar un número")
print("Para ello necesitamos un rango para generar un numero aleatorio")
print("El rango debe ser entre 0 y los numeros enteros positivos")
print("Este rango debe ser determinado por usted :)")
#Se solicita ingresar el limite inferior y superior
num1 = int(input("Ingrese el primer dígito: "))
num2 = int(input("Ingrese el segundo dígito: "))
while num1 > num2:
    print("Para generar un rango correctamente, el 1er número debe ser")
    print("menor que el 2do número, ingrese correctamente los dígitos")
    num1 = int(input("Ingrese nuevamente el primer dígito: "))
    num2 = int(input("Ingrese nuevamente el segundo dígito: "))
guess_num = randint(num1, num2) #Se concideran como lim. superior e inferior el num1 y num2
print("Hora de adivinar el número")
first_attempt = int(input("Ingrese su primer numero para adivinar: "))
if first_attempt == guess_num: #PRIMER INTENTO
    print("Felicitaciones, adivinaste a la primera!")
else:
    if first_attempt > guess_num:
        print("PISTA: El numero que ingresaste es mayor que el correcto")
    else:
        print("PISTA: El numero que ingresaste es menor que el correcto")
    second_attempt = int(input("2do intento, ingrese su numero para adivinar: ")) #SEGUNDO INTENTO
    if second_attempt == guess_num:
        print("Felicitaciones, adivinaste en tu segundo intento")
    else:
        print("Incorrecto")
    if second_attempt > guess_num:
        print("PISTA: El numero que ingresaste es mayor que el correcto")
    else:
        print("PISTA: El numero que ingresaste es menor que el correcto")
    print("Por ser el 2do intento, se te dará una pista extra")
    num_cercano1 = abs(first_attempt - guess_num) #Para que me entregue el valor ABSoluto
    num_cercano2 = abs(second_attempt - guess_num) #Lo mismo que lo de arriba :v
    if num_cercano1 < num_cercano2:
        print(f"El numero correcto esta mas cerca de {first_attempt} que de {second_attempt}")
    elif num_cercano2 < num_cercano1:
        print(f"El numero correcto esta mas cerca de {first_attempt} que de {second_attempt}")
    else:
        print("Ambos numeros estan igual de cerca al numero correcto")

    print("Tercer y último intento")
    third_attempt = int(input("Ingrese su numero para adivinar: ")) #TERCER INTENTO
    if third_attempt == guess_num:
        print("Felicitaciones!, ganaste en tu último intento")
    else:
        print(f"Perdiste, el numero correcto era {guess_num}")