#Generar un numero aleatorio
print("Juego para adivinar un número")
print("Para ello necesitamos un rango para generar un numero aleatorio")
print("El rango debe ser entre 1 y 10")
print("Este rango debe ser determinado por usted :)")
num1 = int(input("Ingrese el primer dígito: "))
num2 = int(input("Ingrese el segundo dígito: "))
while num1 > num2:
    print("Para generar un rango correctamente, el 1er número debe ser")
    print("menor que el 2do número, ingrese correctamente los dígitos")
    num1 = int(input("Ingrese nuevamente el primer dígito: "))
    num2 = int(input("Ingrese nuevamente el segundo dígito: "))

media =  (num1 + num2)/2
ajuste = (num2 - num1)*0.2

if (num1 + num2)%2==0:
    guess_num = int(media + ajuste)
else:
    guess_num = int(media - ajuste)

print("Hora de adivinar el número")
intentos = 0
while intentos < 3:
    intento = int(input("Ingrese nuevo numero para adivinar"))
    intentos +=1
    if intento == guess_num:
        print("Ganaste!")
        break
    if intento > guess_num:
        print("El numero ingresado es mayor al correcto")
    if intento < guess_num:
        print("El numero ingresado es menor al correcto")
if intentos == 3 and intento != guess_num:
    print(f"Fallaste, el número correcto era {guess_num}")