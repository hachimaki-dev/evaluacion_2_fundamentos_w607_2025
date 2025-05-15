import random

print("### Adivina el número ###\n Sigue los siguientes pasos:")

num1=0
num2=0
while num1<=num2:
    num1=int(input("Ingresa un limite inferior:\n"))
    num2=int(input("Ingresa un limite superior:\n"))

num_aleatorio=random.randint(num1,num2)

print("####  Empecemos el juego!!!  ####")

intento1=int(input(("Cual crees que es el número misterioso?\n")))
if intento1!=num_aleatorio:
    if intento1>num_aleatorio:
        print("El numero que ingresaste es mayor al numero misterioso")
    else:
        print("El numero que ingresaste es menor al numero misterioso")
    intento2=int(input(("Cual crees que es el número misterioso?\n")))
    if intento2!=num_aleatorio:
        if intento2>num_aleatorio:
            print("El numero que ingresaste es mayor al numero misterioso")
        else:
            print("El numero que ingresaste es menor al numero misterioso")
    
else:
    print("Has acertado!! Felicidades")



