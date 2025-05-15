from random import randint  

print("-- Adivina el número --")

lim_inf = int(input("Ingrese el límite inferior: "))
lim_sup = int(input("Ingrese el límite superior: "))

if lim_inf > lim_sup:
    print("¡El límite inferior debe ser menor al límite superior!")
    lim_inf = int(input("Ingrese el límite inferior: "))

# Número aleatorio
numero = randint(lim_inf, lim_sup)
print("Se ha generado un número... ¡Adivínalo!")

vidas = 3

intento = int(input("¿Cuál es el número? ")) 

if intento != numero:
    print("Te equivocaste.")
    vidas = vidas - 1

if intento != numero and vidas != 0:
    if intento > numero:
        print("El número que buscas es menor.")
    elif intento < numero:
        print("El número que buscas es mayor.")

    if vidas == 1:
        dif1 = 0
        dif = inf
    
    intento = int(input("¿Cuál es el número? ")) 
