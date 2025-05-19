import random

primer_num_menor = int(input("ponga un numero:"))
segundo_num_superior = int(input("ponga otro numero mayor al primero:"))

num_aleatorio = random.randint(primer_num_menor, segundo_num_superior)
print("el numero es:")

primer_intento = int(input("ponga el numero que crea que salio:"))


if num_aleatorio == primer_intento:
    print("felicidades hacertaste")
elif num_aleatorio > primer_intento:
    print("el numero aleatorio es mayor al que pusiste")
elif num_aleatorio < primer_intento:
    print("el numero aleatorio es menor al que pusiste ")


num_aleatorio2 = random.randint(primer_num_menor, segundo_num_superior)
segundo_intento = int(input("ponga el numero que crea que salio:"))
    
if num_aleatorio2 == segundo_intento:
    print("felicidades hacertaste")
elif num_aleatorio2 > segundo_intento:
        print("el numero aleatorio es mayor al que pusiste se hacerca a",(segundo_intento - num_aleatorio2))
elif num_aleatorio2 < segundo_intento:
        print("el numero aleatorio es menor al que pusiste se hacerca a",(segundo_intento - num_aleatorio))


primer_num_menor = int(input("intente denuevo, ponga un numero:"))
segundo_num_superior = int(input("ponga otro numero mayor al primero:"))

num_aleatorio3 = random.randint(primer_num_menor, segundo_num_superior)
tercer_intento = int(input("ponga el numero que crea que salio:"))

if num_aleatorio3 == tercer_intento:
    print("felicidades hacertaste")
elif num_aleatorio3 > tercer_intento:
        print("perdiste")
elif num_aleatorio3 < tercer_intento:
        print("perdiste")




