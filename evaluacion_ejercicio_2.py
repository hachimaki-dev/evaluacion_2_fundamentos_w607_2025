from random import randint
numero_limite_inferior = int(input("digite un numero: "))
numero_limite_superior = int(input("digite un numero: "))
vidas = 3
if numero_limite_inferior >= numero_limite_superior:
    print("error el primer numero debe ser menor que el segundo ")
else:
    print("los numeros ingresados estan correctos")
numero_magico = randint(numero_limite_inferior,numero_limite_superior)
print("tienes tres intentos")
print("en que numero estoy pensando")
intento_1 = int(input("digite su primer intento: "))
if intento_1 == numero_magico:
    print("lo lograstes estaba pensando en ese numero: ", numero_magico)
    print("felicidades ganaste ")
else:
    print(" casi pero ese no era el numero que estaba pensando ")
    vidas = vidas - 1
    print("perdiste una vida, te quedan:  ",vidas)
    if intento_1 > numero_magico:
        print("te dare una pista: el numero que estoy pensando es menor que el numero que digitaste ")
    else:
        print("te dare una pista: el numero que estoy pensando es mayor que el numero que digitaste ")

intento_2 = int(input("digite se segundo intento: "))
if intento_2 == numero_magico:
    print("lo lograstes en tu segundo intento, estaba pensando en ese numero: ", numero_magico)
    
else:
    print("otra vez no le atinaste pero no te preocupes te queda una vida ")
    vidas = vidas - 1
    print("perdiste otra vida te quedan: ",vidas)
    pista_2 = intento_1 - numero_magico 
    pissta_2 = intento_2 - numero_magico
    if pista_2 < pissta_2 :
        print("te dare otra pista: el intento 2 esta mas cerca del numero magico que el intento 1 ")
    else:
        print("te dare otra pista: el intento 1 esta mas cerca del numero magico que el intento 2 ")

    if intento_2 > numero_magico:
        print("te dare una pista: el numero que estoy pensando es menor que el numero que digitaste ")
    else:
        print("te dare una pista: el numero que estoy pensando es mayor que el numero que digitaste ")
intento_3 = int(input("digite su ultimo intento: "))
if intento_3 == numero_magico:
    print("lo lograste en tu ultima bala sjsjsjsj")
    print("bien hecho felicidades ")

else:
    vidas = vidas - 1 
    print("te quedaste sin vidas: ", vidas)
    print("perdiste :(, no lograste adivinar el numero magico")

    print("el numero magico era el:", numero_magico )
