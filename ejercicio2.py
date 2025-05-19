from random import randint

intentos = 0
FinJuego = False

if intentos == 3:
    FinJuego = True

print("Bienvenido a este juego de adivinanzas")

num1 = int (input("Ingresa un numero: "))
num2 = int (input("Ingresa otro numero: "))

numero = randint(num1,num2)  

if num1 > num2:
    print("El numero 1 tiene que ser menor al numero 2")
elif num1 < num2:
    print("Iniciando adivinanza...")    

#intento 1

adivinanza1 = int (input("Ingrese numero: ")) 

print ("Cargando...")

if adivinanza1 == numero:
    print("Felicitaciones, adivinaste.")
    FinJuego = True

else:
    print("Cerca")

if adivinanza1 < numero:
    print("Pista: el numero es mayor")
elif adivinanza1 > numero:
    print("Pista: el numero es menor")

#intento 2    

intentos = intentos + 1

adivinanza2 = int (input("Ingrese numero: "))

print ("Cargando...")

if adivinanza2 == numero:
    print("Felicitaciones, adivinaste.")
    FinJuego = True
else:
    print("Cerca")

if adivinanza2 < numero:
    print("Pista: el numero es mayor")
elif adivinanza2 > numero:
    print("Pista: el numero es menor")

cerca1 = abs(numero - adivinanza1)
cerca2 = abs(numero - adivinanza2)

if cerca1 < cerca2:
    print(f"El numero {adivinanza1} esta mas cerca que {adivinanza2}")
elif cerca1 > cerca2:
    print(f"El numero {adivinanza2} esta mas cerca que {adivinanza1}") 
else:
    print(f"{adivinanza1} y {adivinanza2} son los mismos")       


intentos = intentos + 1

#intento 3

adivinanza3 = int (input("Ingrese numero: "))

print ("Cargando...")

if adivinanza3 == numero:
    print("Felicitaciones, adivinaste.")
    FinJuego = True
else:
    print("El numero era:", numero, "Suerte para la proxima")

intentos = intentos + 1

if FinJuego == True:
    print ("Gracias por jugar")
