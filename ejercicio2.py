import random

limite_inferior = int(input("Ingrese el limite inferior : \n"))
limite_superior = int(input("Ingrese el limite superior: \n"))

if limite_inferior > limite_superior:
    print("El limite inferior no puede ser mayor que el superior.")
else:
    num_al = random.randint(limite_inferior, limite_superior)
    num_ingresado_1 = int(input("Adivine el numero: \n"))
    
    intentos = 3

    if num_ingresado_1 == num_al:
            print("Has ganado!")
    else:
        intentos -= 1
        if num_ingresado_1 > num_al:
            print("El numero es menor ")
        elif num_ingresado_1 < num_al:
            print("El numero es mayor")
            print(f"Tienes {intentos} intentos")

        num_ingresado_2 = int(input("Intente de nuevo: \n"))
        
        if num_ingresado_2 == num_al:
            print("Has ganado!")
        else:
            intentos -= 1
            if num_ingresado_2 > num_al:
                print("El numero es menor ")
            elif num_ingresado_2 < num_al:
                print("El numero es mayor")

            dif1 = num_ingresado_1 - num_al if num_ingresado_1 > num_al else num_al - num_ingresado_1
            dif2 = num_ingresado_2 - num_al if num_ingresado_2 > num_al else num_al - num_ingresado_2

            if dif1 < dif2:
                print("Pista: El primer numero que ingresaste esta mas cerca del numero a adivinar")
            elif dif1 > dif2:
                print("Pista: El segundo numero que ingresaste esta mas cerca del numero a adivinar")
            else:
                print("Ambos estuvieron igual de cerca")
                print(f"Te quedan {intentos} intentos")

            num_ingresado_3 = int(input("Ultimo intento: \n"))

            if num_ingresado_3 == num_al:
                print("Has adivinado el numero!")
            else:
                print(f"El numero era {num_al}, Has perdido")
        