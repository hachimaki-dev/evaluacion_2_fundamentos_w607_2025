import random

limite_inferior = int(input("Ingresa el limite inferior"))
limite_superior = int(input("Ingresa el limite superior"))

numero_aleatorio = random.randint(limite_inferior, limite_superior)
print("Numero aleatorio: ", numero_aleatorio)