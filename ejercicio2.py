import random

try:
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    if num1 > num2:
        print("El primer número tiene que ser menor al segundo digitado. Vuelva a ejecutar el programa.")
        exit()
except ValueError:
    print("Error detectado: Tiene que ingresar un valor numérico. Vuelva a ejecutar el programa.")
    exit()

numelegido = random.randint(num1, num2)
intentos = 3
pista = 0
print("\n")
print(f"———————————— Es hora de adivinar el número entre los rangos que elegiste, o sea, entre {num1} y {num2} ————————————")
print("\n")

#Intento 1
intnum1 = int(input("Ingresa el número que crees que es la respuesta: "))

if intnum1 == numelegido:
    print(f"El número que elegiste fue {intnum1}, y el número a adivinar era {numelegido}, felicidades!")
    print("Fin del juego!")
    exit()

elif intnum1 != numelegido:
    intentos -= 1
    print(f"Incorrecto, el número no es {intnum1}! Inténtalo de nuevo, te quedan {intentos} intentos.")
    if intnum1 < numelegido:
        print("El número a adivinar es mayor que el cual digitaste.")
    elif intnum1 > numelegido:
        print("El numero a adivinar es menor que el cual digitaste.")

#Intento 2
intnum2 = int(input("Ingresa el número que crees que es la respuesta: "))

if intnum2 == numelegido:
    print(f"El número que elegiste fue {intnum2}, y el número a adivinar era {numelegido}, felicidades!")
    print("Fin del juego!")
    exit()

elif intnum2 != numelegido:
    intentos -= 1
    print(f"Incorrecto, no es {intnum2} como habías dicho! Inténtalo de nuevo, te queda {intentos} intento.")
    if intnum2 < numelegido:
        print("El número a adivinar es mayor que el cual digitaste.")
    elif intnum2 > numelegido:
        print("El numero a adivinar es menor que el cual digitaste.")

# Intento 3
intnum3 = int(input("Ingresa el número que crees que es la respuesta: "))

if intnum3 != numelegido:
    intentos -= 1
    print(f"Incorrecto, no es {intnum3} como habías dicho!")
    print(f"Se te han acabado los intentos. El número a adivinar era {numelegido} y tú pusiste {intnum3}.")
    print(f"Debido a que quedan {intentos} intentos, el juego ha acabado.")
    exit()

elif intnum3 == numelegido:
    print(f"El número que elegiste fue {intnum3}, y el número a adivinar era {numelegido}, felicidades!")
    print("Fin del juego!")
    exit()


# Lo que no logré resolver nunca fue lo de indicar si el número estaba más cerca o más lejos del número digitado