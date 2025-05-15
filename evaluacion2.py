import random

print("Ingrese dos números enteros que definan un rango.")
num1 = int(input("Ingrese el límite inferior: "))
num2 = int(input("Ingrese el límite superior: "))

if num1 >= num2:
    print("Error: El límite inferior debe ser menor que el límite superior.")
else:
    punto_medio = (num1 + num2) / 2
    ajuste = (num2 - num1) * 0.2
    numeroSecreto = random.uniform(punto_medio - ajuste, punto_medio + ajuste)
    numeroSecreto = round(numeroSecreto)
    intentos = 3
    #Uso del random uniform para dar un rango a números flotantes(con decimales).

    print("¡Intenta adivinar el número generado!")
    intento1 = int(input("Intento 1: Ingrese su número: "))

    if intento1 == numeroSecreto:
        print("¡Felicitaciones, pudiste adivinar!")
    else:
        if intento1 < numeroSecreto:
            print("El número es mayor.")
        else:
            print("El número es menor.")

        intento2 = int(input("Intento 2: Ingrese su número: "))

        if intento2 == numeroSecreto:
            print("¡Felicitaciones, pudiste adivinar!")
        else:
            if intento2 < numeroSecreto:
                print("El número es mayor.")
            else:
                print("El número es menor.")
            
            intento3 = int(input("Intento 3: Ingrese su número: "))

            if intento3 == numeroSecreto:
                print("¡Felicitaciones, pudiste adivinar!")
            else:
                print(f"Perdiste. El número correcto era {numeroSecreto}.")