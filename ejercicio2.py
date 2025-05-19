from random import randint

numero = randint(1, 10)

print(numero)
vida = 3
print("BIENVENIDO")
print("ADIVINA EL NUMERO ENTRE 1 Y 10!!")
adivinar1 = int(input("Cual crees que es el numero?:"))

if adivinar1 == numero:
    print("FELICIDADES!")
elif adivinar1 < numero:
    vida -= 1
    print("El numero es mayor")
elif adivinar1 > numero:
    vida -= 1
    print("El numero es menor")


adivinar2 = int(input("Cual sera ahora el numero:"))

if adivinar2 == numero:
    print("FELICIDADES")
elif adivinar2 < numero:
    vida -= 1
    print("El numero es mayor")
elif adivinar2 > numero:
    vida -= 1
    print("El numero es menor")

if adivinar2 < adivinar1 < numero:
    print(f"El numero {adivinar1} esta mas cerca")
elif adivinar2 > adivinar1 > numero:
    print(f"El numero {adivinar1} esta mas cerca")
elif adivinar1 < adivinar2 < numero:
    print(f"EL numero {adivinar2} esta mas cerca")
elif adivinar1 > adivinar2 > numero:
    print(f"El numero {adivinar2} esta mas cerca")

adivinar2 = int(input("Cual sera tu ultimo numero:"))

if adivinar2 == numero:
    print(f"FELICIDADES EL NUMERO ERA {numero}")
elif adivinar2 != numero:
    vida -= 1
    print(f"Perdiste el numero era {numero}")




    

    

    


    


  

