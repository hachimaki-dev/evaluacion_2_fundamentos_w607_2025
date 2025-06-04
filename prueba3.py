#variables globales
persn_esq_incompleto = 0
persn_esq_completo = 0
dosis_esq_completo = 3

#While para ingresar cantidad de personas 
while True:
    try:
        num_personas = int(input("Ingrese la cantidad de personas a registrar: "))
        break        
    except ValueError:
        print("Debe ingresar un número entero")