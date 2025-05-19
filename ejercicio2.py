import random

print("Bienvenido a un juego de adivinanzas")
print("Ingresa dos números, el primero debe ser menor que el segundo")

num1 = int(input("Ingrese el primer número (menor): "))
num2 = int(input("Ingrese el segundo número (mayor): "))

num_secret = random.randint(num1, num2)
intento = 0
intent_prev = []

while intento < 3:
    intento += 1
    num = int(input("Adivine el número: "))
    intent_prev.append(num)
    
    if num == num_secret:
        print("Felicidades, ha ganado")
        break
    else:
        if num < num_secret:
            print("El número es mayor")
        else:
            print("El número es menor")
            
        if intento == 2:
            if len(intent_prev) >= 2:
                intento1 = intent_prev[0]
                intento2 = intent_prev[1]
                
                if num_secret - intento1 < 0:
                    distancia1 = -(num_secret - intento1)
                else:
                    distancia1 = num_secret - intento1
                    
                if num_secret - intento2 < 0:
                    distancia2 = -(num_secret - intento2)
                else:
                    distancia2 = num_secret - intento2
                    
                if distancia1 <= distancia2:
                    print(f"Pista: El número está más cerca de tu primer intento ({intento1})")
                else:
                    print(f"Pista: El número está más cerca de tu segundo intento ({intento2})")
            
        if intento == 3:
            print("GAME OVER")
            print(f"El número correcto era: {num_secret}")
    