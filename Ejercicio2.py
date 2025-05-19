## Instrucciones del ejercicio N°2

## Objetivo

#Desarrollar un programa en **Python** que permita:

#1. **Generar un número aleatorio** dentro de un rango definido por el usuario.
#2. Simular un **juego de adivinanza** con hasta **3 intentos**.

#---

## Requisitos del Programa

#El programa debe hacer lo siguiente:

#1. Solicitar al usuario **dos números enteros** que representen el **límite inferior y superior** de un rango numérico.

#   * El primer número ingresado (límite inferior) debe ser **menor** que el segundo (límite superior).

#2. Usar la función `randint()` para **generar un número aleatorio** dentro del rango indicado.


from random import randint
bandera = False
print(" ")
print("---------------------------------------------------------------------")
print("---------------- Bienvenido al juego de adivinanza¡ -----------------")
print("----- Ingrese el límite inferior y superior del rango numérico. -----")
print("---------------------------------------------------------------------")
print(" ")
print("Recuerda que el primer número debe ser menor que el segundo.")
print(" ")
print("---------------------------------------------------------------------")
Lim_inferior = int(input("Ingrese el primer Numero (Lim_Inferior): "))
print("---------------------------------------------------------------------")
Lim_superior = int(input("Ingrese el segundo Numero (Lim_Superior): "))
print("---------------------------------------------------------------------")
print(" ")

if Lim_inferior >= Lim_superior:
    print(" ")
    print("--- [ El límite inferior debe ser menor que el límite superior. ] ---")
    print(" ")
    print(" ")
    print("---------------------------------------------------------------------")
else:
    Num_aleatorio_LOL = randint(Lim_inferior, Lim_superior)
    print(f"Un número aleatorio ha sido generado entre los numeros {Lim_inferior} y {Lim_superior}.")
    print(" ")
    print("---------------------------------------------------------------------")

    Num_intentos = 3
    while Num_intentos > 0:
        Intento_usuario = int(input(f"Tienes {Num_intentos} intentos restantes. Ahora adivina el número: "))
        print("---------------------------------------------------------------------")
        print(" ")
        
        
        if Intento_usuario == Num_aleatorio_LOL:
            print("---------------------------------------------------------------------")
            print("¡Felicidades! Has adivinado el número¡¡ !Bien hecho¡.")
            print(" ")
            print("¡Gracias por jugar!")
            print("---------------------------------------------------------------------")
            bandera = True
            break
        elif Intento_usuario < Num_aleatorio_LOL:
            if Num_intentos > 1:
                print("El número es mayor, estas muy abajo, compañero, !no te rindas¡.")
        else:
                print("El número es menor, !Bajas más¡")
        
        Num_intentos -= 1

    if not bandera:
        print("---------------------------------------------------------------------")
        print(f"! Lo lamento, has agotado tus intentos. El número era {Num_aleatorio_LOL} ¡")
        print("!Intentalo de nuevo¡ :D. ")
        print(" ")
        print(" ¡Gracias por jugar! ")
        print("---------------------------------------------------------------------")

    
