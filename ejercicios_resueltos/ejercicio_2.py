from random import randint
import random
print("Lo que debe hacer es adivinar el valor del numero al azar del 1 al 10 solo tiene 3 intentos suerte")

numero_misterioso = random.randint(1,10)

intentos = 3
for intentos in range(1, intentos +1):

 try:
   
   adivina = int(input(f"intento {intentos}:"))
 except ValueError:
  print("igrese numero valido")
 continue

if adivina == numero_misterioso:
 print("Lo lograste felicidades ")

else:
    intentos = 2
    diferencia = abs(intentos - numero_misterioso)
    if diferencia <=3:

       print("casi aciertas")
    else:
       print("no estas muy cerca")
    if intentos < intentos:
        print("intenta de nuevo")
    else:
        print(f"lo siento fallaste el numero era {numero_misterioso}")