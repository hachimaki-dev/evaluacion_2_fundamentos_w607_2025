import random

limite_inferior = int(input("Ingrese el limite inferior : \n"))
limite_superior = int(input("Ingrese el limite superior: \n"))

if limite_inferior > limite_superior:
    print("El limite inferior no puede ser mayor que el superior.")
else:
    num_al = random.randint(limite_inferior, limite_superior)
    num_ingresado = int(input("Adivine el numero: \n"))
    
    intentos = 3
    
    while intentos > 0:
        if num_ingresado < num_al:
            print("El numero es mayor ")
            intentos -= 1
            print(f"Tienes {intentos} intentos")
        elif num_ingresado > num_al:
            print("El numero es menor ")
            intentos -= 1
            print(f"Tienes {intentos} intentos")
        else:
            print("Has adivinado el numero!")
            break
        num_ingresado = int(input("Intente de nuevo: \n"))

        if intentos == 0:
            print(f"El numero era {num_al}, Has perdido")
        