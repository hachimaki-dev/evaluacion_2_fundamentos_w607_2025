from random import randint  

print("-- Adivina el número --")

lim_inf = int(input("Ingrese el límite inferior: "))
lim_sup = int(input("Ingrese el límite superior: "))

if lim_inf > lim_sup:
    print("¡El límite inferior debe ser menor al límite superior!")
    lim_inf = int(input("Ingrese el límite inferior: "))

# Número aleatorio
numero = randint(lim_inf, lim_sup)
print(f"Se ha generado un número entre {lim_inf} y {lim_sup}... ¡Adivínalo!")
print(numero)

adivinado = False

# Primer intento
intento1 = int(input("1.- Ingresa tu intento: ")) 

if intento1 == numero:
    adivinado = True
else:
    print("No acertaste.")
    if intento1 > numero:
        print("El número que buscas es menor.")
    elif intento1 < numero:
        print("El número que buscas es mayor.")

# Segundo intento
if not adivinado:
    intento2 = int(input("2.- Ingresa tu intento: ")) 

    if intento2 == numero:
        adivinado = True
    else:
        print("No acertaste.")
        if intento2 > numero:
            print("El número que buscas es menor.")
        elif intento2 < numero:
            print("El número que buscas es mayor.")  
        # Calcula diferencias
        dif1 = abs(numero - intento1)
        dif2 = abs(numero - intento2)
        if dif1 < dif2:
            print(f"Pista: El primer número ingresado >>{intento1}<< estaba más cerca.")
        elif dif1 > dif2:
            print(f"Pista: El segundo número ingresado >>{intento2}<< estaba más cerca.")

# Tercer intento
if not adivinado:
    intento3 = int(input("3.- Ingresa tu intento final: "))

    if intento3 == numero:
        adivinado = True
    else:
        print(f"Perdiste, el número era: {numero}")
        print("Fin del juego.")

if adivinado:
    print("¡Felicidades! Adivinaste.")
