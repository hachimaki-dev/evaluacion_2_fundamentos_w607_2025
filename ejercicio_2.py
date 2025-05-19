## Importar libreria ##
import random

print("### Adivina el número ###\nSigue los siguientes pasos:")

## Variables y filtro ##
num1=0
num2=0
while num1>=num2:
    num1=int(input("Ingresa un límite inferior:\n"))
    num2=int(input("Ingresa un límite superior:\n"))

## Generar el Número aleatorio ##
num_aleatorio=random.randint(num1,num2)

print("####  Empecemos el juego!!!  ####")
print("----   Solo tienes 3 intentos   ----")

## Intento 1 ##
intento1=int(input(("¿Cual crees que es el número misterioso?\n")))
if intento1!=num_aleatorio:
    ## Pista menor o mayor ##
    print("Fallaste, aquí te va una pista: ")
    if intento1>num_aleatorio:
        print("El número que ingresaste es mayor al número misterioso")
    else:
        print("El número que ingresaste es menor al número misterioso")
    ## Intento 2 ##
    intento2=int(input(("¿Cual crees que es el número misterioso?\n")))
    if intento2!=num_aleatorio:
        print("Has fallado, te queda solo un intento, aqui te van algunas pistas:")
        ## Pista menor o mayor ##
        if intento2>num_aleatorio:
            print("El número que ingresaste es mayor al número misterioso")
        else:
            print("El número que ingresaste es menor al número misterioso")
        ## Pista intento más cercano ##
        comp1=abs(num_aleatorio - intento1) ## comparación con intento 1
        comp2=abs(num_aleatorio - intento2) ## comparación con intento 2
        if comp1 < comp2:
            print(f"El número {intento1} esta mas cerca del número misterioso")
        elif comp1 == comp2:
            print("Los dos números que ingresaste estan a la misma distancia del número misterioso")
        else:
            print(f"El número {intento2} esta mas cerca del número misterioso")

        ## Intento 3 ##
        intento3=int(input(("¿Cual crees que es el número misterioso?\n")))
        if intento3==num_aleatorio:
            print("Has acertado!! Felicidades")
        else:
            print(f"Has perdido! El número misterioso es: {num_aleatorio}")
    else:
        print("Has acertado!! Felicidades")
else:
    print("Has acertado!! Felicidades")



