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

#ahora quiero que definas una variable como bandera = False, entonces una vez se acaben los intentos, no repitas antes de el, 
# el mensaje de "El número es mayor, estas muy abajo, compañero, !no te rindas¡." o "El número es menor, !Bajas más¡"


from random import randint
bandera = False

print("Bienvenido al juego de adivinanza¡")
print("Ingrese el límite inferior y superior del rango numérico.")

lim_inferior = int(input("Primer Numero (Lim_Inferior): "))
lim_superior = int(input("Segundo Numero (Lim_Superior): "))

if lim_inferior >= lim_superior:
    print("El límite inferior debe ser menor que el límite superior.")
else:
    Num_aleatorio_LOL = randint(lim_inferior, lim_superior)
    print(f"Un número aleatorio ha sido generado entre los numeros {lim_inferior} y {lim_superior}.")

    Num_intentos = 3
    while Num_intentos > 0:
        Intento_usuario = int(input(f"Tienes {Num_intentos} intentos restantes. Ahora adivina el número: "))
        
        if Intento_usuario == Num_aleatorio_LOL:
            print("¡Felicidades! Has adivinado el número¡¡ !Bien hecho¡.")
            bandera = True
            break
        elif Intento_usuario < Num_aleatorio_LOL:
            if Num_intentos > 1:
                print("El número es mayor, estas muy abajo, compañero, !no te rindas¡.")
        else:
            if Num_intentos > 1:
                print("El número es menor, !Bajas más¡")
        
        Num_intentos -= 1

    if not bandera:
        print(f"Lo lamento, has agotado tus intentos. El número era {Num_aleatorio_LOL}, Intentalo de nuevo¡ :D.")

    


        
