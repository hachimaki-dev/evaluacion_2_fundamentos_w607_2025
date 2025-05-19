from random import randint  # Importa la función randint
print("Juego de adivinar el numero. Ingrese un rango numerico")
num1 = int(input("Inrgese numero 1: "))
num2 = int(input("Inrgese numero 2: "))

while num1 >= num2:
    num1 = int(input("Inrgese numero 1 menor a numero 2: "))

numero = randint(num1, num2)  # Genera un número aleatorio entre num1 y num2 (incluyéndolos)
print(num1, num2, numero)

print("Tienes 3 intenteos para adivinar el numero aleatorio dentro de ese rango")

i=0
for i in range(3):
    adivinar =int(input("Ingrese un numero para adivinar el numero aleatorio: "))

    if adivinar == numero:  
        print("Felicidades adivinaste el numero")
        exit()
    elif adivinar > numero:
        print("El numero a advinar es menor")
    else:
        print("El numero a advinar es mayor")

  ##-----------------------------------  validacion 2 parte  ee- e e e---------------------------------------------------------------##

    if i == 0:
        intento1= abs(numero - adivinar) 

    elif i == 1:
        intento2= abs(numero - adivinar)

        if intento1 < intento2:
            print("Pista: El intento 1 estubo mas serca del numero secreto")
        elif intento2 < intento1:
            print("Pista: El intento 2 estubo mas serca del numero secreto")
        else:
            print("Pista: Los dos intento estuvieron a la misma distancia de sercania")

print("Juego terminado fallaste los 3 intentos el numero era",numero)
