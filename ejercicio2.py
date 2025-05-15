import random

print("Vamos a jugar un juego de adivinanza")
print("Para este juego tienes solo 3 intentos")
print("Elige dos números (uno mayor que el otro)")

n1 = int(input("Ingresa el primer número (el número menor)\n"))
n2 = int(input("Ingresa el segundo número (el número mayor)\n"))

nran = random.randint(n1,n2)

int1 = int(input("Intenta adivinar\n"))
if int1 < nran:
    print("El número es mayor")
elif int1 > nran:
    print("El número es menor")

int2 = int(input("Intenta de nuevo\n"))
if int2 < nran:
    print("El número es mayor")
elif int2 > nran:
    print("El número es menor")