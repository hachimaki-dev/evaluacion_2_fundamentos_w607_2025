from random import randint

print("Bienvenido al juego de la adivinanza en este juego se creara un numero aleatorio entre el numero menor y el numero mayor  solo tienes 3 vidas")
print("Antes que nada el numero menor no puede ser mas grande que el mayor ")

numero_menor = int(input("Ingresa el numero menor "))
numero_mayor = int(input("Ingresa el numero mayor "))

numero_aleatorio = randint(numero_menor, numero_mayor)

if numero_menor >= numero_mayor:
    print("el numero menor no puede ser mas grande")
else:
    print(f"un numero random a sido generado entre {numero_menor}, {numero_mayor} buena suerte")
    intento1 = int(input("Adivina el numero "))
if intento1 == numero_aleatorio:
    print("felicidades adivinaste el numero aleatorio ")
    
elif intento1 != numero_aleatorio:
    print("Incorrecto vuelve a intentarlo ")
    intento2 = int(input("Adivina el numero"))
if intento2 == numero_aleatorio:
    print("Felicidades adivinaste el numero al segundo intento ")
    
elif intento2 != numero_aleatorio:
    print("Incorrecto intentalo de nuevo")
if intento2 > numero_aleatorio:
    print("Pista el numero aleatorio es mayor al que introdujiste")
    intento3 = int(input("Adivina el numero "))
if intento2 < numero_aleatorio:
    print("Pita el numero aleatorio es menor al que introdujiste")
    intento3 = int(input("Adivina el numero "))
if intento3 == numero_aleatorio:
    print("Felicidades adivinaste el numero al tercer intento")
    
elif intento3 != numero_aleatorio:
    print("Incorrecto te quedaste sin vidas")