print("Bienvenido al juego de la adivinanza")

num_inf = int(input("Ingrese el limite inferior: "))
num_sup = int(input("Ingrese el limite superior: "))

while num_inf >= num_sup:
    print("Error, el numero inferior debe ser menor al numero superior")
    num_inf = num_inf = int(input("Ingrese el limite inferior: "))
    num_sup = num_sup = int(input("Ingrese el limite superior: "))

from random import randint 
num_random = randint(num_inf, num_sup)  

adivinado = False

distanciaNumMenor = 0
distanciaNumMayor = 0

for intentos in range(1,4):

    intento = int(input("Intente adivinar el número: "))

    if intento == num_random:
        print("Felicidades, adivinaste el numero")
        adivinado = True
        break

    elif intentos == 1 > num_random:
        print("Pista 1, el numero que buscas es menor")
    else:
        print("Pista 1, el numero que buscas es mayor")

    if intentos == 2:
        distanciaNumMenor = num_random - num_inf
        distanciaNumMayor = num_random - num_sup

        if distanciaNumMayor < distanciaNumMenor:
             print("Pista 2, el numero está más cerca del numero ", num_sup)
        else:
             print("Pista 2, el numero está más cerca del numero ", num_inf)

if adivinado == False:
    print("Perdiste, el numero que buscabas era: ", num_random)
