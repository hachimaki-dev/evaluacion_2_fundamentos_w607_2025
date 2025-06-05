#variables globales
persn_esq_incompleto = 0
persn_esq_completo = 0
dosis_esq_completo = 3
cont_dosis = 0

#While para ingresar cantidad de personas 
while True:
    try:
        num_personas = int(input("Ingrese el numero de personas que desea registrar: "))
        break        
    except ValueError:
        print("Debe ingresar un número entero")

#Bucle para preguntar por cada persona que se ingreso la cantidad de dosis que ha recibido en el vacunatorio
for i in range(num_personas):
        
   while True:
       
        if cont_dosis < num_personas:
            try:
                dosis = int(input("Ingrese las dosis que ha recibido: "))
                cont_dosis = cont_dosis + 1
                print(f"Cantidad de veces {cont_dosis}")
            
            except ValueError:
                print("Debe ingresar un número entero")
        else:
            print(f"Numero de personas es {num_personas}")
            break