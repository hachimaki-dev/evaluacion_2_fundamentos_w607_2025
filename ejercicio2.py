import random

intentos = 3
numero1 = int(input("Ingrese un número entre 1 y 10: "))

while True:
    numero2 = int(input("Adivina un número entre 1 y 10. Ojito! Tiene que ser mayor al anterior: "))
    if numero2 > numero1:
        break
    print("Te dije que número mayor al anterior, intenta de nuevo")

calculo_div = numero1 + numero2 / 2
calculo_mul = numero1 - numero2 * 0.2
