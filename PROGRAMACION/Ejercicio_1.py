#NUMEROS PRIMOS 

def es_primo(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

while True:
    try:
        numero = int(input(f"Ingrese cuantas verificaciones desea realizar: "))
        if numero > 0:
            break
        else:
            print("Por favor, ingrese un número mayor que cero.")
    except ValueError:
        print("Por favor, debes ingresar un número entero.")
primos = 0
for i in range(numero):
    while True:
        try:
            num = int(input(f"Ingrese el numero {i + 1}: "))
            break
        except ValueError:
            print("Por favor, debes ingresar un número entero.")
    if es_primo(num):
        print(f"{num} es un numero primo.")
        primos += 1
    else:
        print(f"{num} no es un numero primo.")
print(f"Se han verificado {numero} numeros, de los cuales {primos} son primos.")

# Fin del ejercicio