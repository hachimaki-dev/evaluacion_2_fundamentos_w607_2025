import random

primer_num_menor = int(input("ponga un numero:"))
segundo_num_superior = int(input("ponga otro numero mayor al primero:"))

num_aleatorio = random.randint(primer_num_menor, segundo_num_superior)
print("el numero es:")


primer_intento = int(input("ponga el numero que crea que salio:"))


if primer_intento == num_aleatorio:
    print("felicidades acertaste")
elif primer_intento > num_aleatorio:
    print("el numero es mayo intente denuevo:")
elif primer_intento < num_aleatorio:
    print("el numero es menor intente denuevo:")
else:
    print("no hacertaste")
