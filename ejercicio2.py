#Utilizar la libreria de random para importar el numero aleatorio
from random import randint

# Menu del juego
print("----Bienvenidos a el juego adivina mi numero secreto----")
print("----Te pedire 2 numeros y tendras que adivinar el numero secreto----")
print("----el segundo numero ingresado debe ser mayor al primero ----")
# Damos valor a los numeros
Numero1 = int(input("Ingresa el primer numero : "))
Numero2 = int(input("Ingresa el segundo numero : "))
Numero_Secreto = randint(Numero1 , Numero2)

#si el usuario ingresa un numero menor el programa dara un error
if Numero1 < Numero2:


#que empiece el juego 
#Primer intento

    print("Adivina mi numero secreto te quedan 3 vidas")
    Primer_Intento = int(input("Ingresa el numero secreto: "))
    if Primer_Intento == Numero_Secreto:
        print("Felicidades has adivinado el numero secreto")
    else:
        if Primer_Intento < Numero_Secreto:
         print("El numero secreto es mayor") 
        elif Primer_Intento > Numero_Secreto:
         print("El numero secreto es menor")

    #segundo intento

    print("Intenta nuevamente te quedan 2 vidas")
    Segundo_Intento = int(input("Ingresa el numero secreto: "))
    if Segundo_Intento == Numero_Secreto:
        print("Felicidades has adivinado el numero secreto")
    else:
         if Segundo_Intento < Numero_Secreto:
          print("El numero secreto es mayor")
         elif Segundo_Intento > Numero_Secreto:
          print("El numero secreto es menor")

    # calcular ultima pista 
    #se calcula la distancia que hay de lo intentos al numero secreto
    if Primer_Intento > Numero_Secreto:
        Distancia1 = Primer_Intento - Numero_Secreto
    else:
        Distancia1 = Numero_Secreto - Primer_Intento

    if Segundo_Intento > Numero_Secreto:
        Distancia2 = Segundo_Intento - Numero_Secreto
    else:
        Distancia2 = Numero_Secreto - Segundo_Intento

    #Ultima pista 

    if Distancia1 < Distancia2:
        print(f"El numero esta mas cerca de  {Primer_Intento} que de {Segundo_Intento}")
    elif Distancia2 < Distancia1:
        print(f"El numero esta mas cerca de {Segundo_Intento} que de {Primer_Intento}")
    else:
        print("Ambos numeros esta igual de cerca")

    # ultimo intento y cierre del programa
        print ("Te queda un ultimo intento")
        UltimoIntento = int(input("Ingrese el numero secreto: "))
        if UltimoIntento == Numero_Secreto:
            print(" Felicidades has adivinado el numero secreto")
        else:
            print(" Has perdido el numero secreto es", Numero_Secreto)

else:
    print("elige un numero mayor")